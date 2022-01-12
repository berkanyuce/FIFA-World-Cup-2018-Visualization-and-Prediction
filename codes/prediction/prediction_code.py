import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from utilites.data_loading import DATADIR

#Links featuring the strengths of national teams in FIFA games 2004-2017
urls = ["https://www.fifaindex.com/teams/fifa05_1/?type=1",
        "https://www.fifaindex.com/teams/fifa05_1/?page=2&type=1",
        "https://www.fifaindex.com/teams/fifa06_2/?type=1",
        "https://www.fifaindex.com/teams/fifa06_2/?page=2&type=1",
        "https://www.fifaindex.com/teams/fifa07_3/?type=1",
        "https://www.fifaindex.com/teams/fifa07_3/?page=2&type=1",
        "https://www.fifaindex.com/teams/fifa08_4/?type=1",
        "https://www.fifaindex.com/teams/fifa08_4/?page=2&type=1",
        "https://www.fifaindex.com/teams/fifa09_5/?type=1",
        "https://www.fifaindex.com/teams/fifa09_5/?page=2&type=1",
        "https://www.fifaindex.com/teams/fifa10_6/?type=1",
        "https://www.fifaindex.com/teams/fifa10_6/?page=2&type=1",
        "https://www.fifaindex.com/teams/fifa11_7/?type=1",
        "https://www.fifaindex.com/teams/fifa11_7/?page=2&type=1",
        "https://www.fifaindex.com/teams/fifa12_8/?type=1",
        "https://www.fifaindex.com/teams/fifa12_8/?page=2&type=1",
        "https://www.fifaindex.com/teams/fifa13_11/?type=1",
        "https://www.fifaindex.com/teams/fifa13_11/?page=2&type=1",
        "https://www.fifaindex.com/teams/fifa14_12/?type=1",
        "https://www.fifaindex.com/teams/fifa14_12/?page=2&type=1",
        "https://www.fifaindex.com/teams/fifa15_16/?type=1",
        "https://www.fifaindex.com/teams/fifa15_16/?page=2&type=1",
        "https://www.fifaindex.com/teams/fifa16_19/?type=1",
        "https://www.fifaindex.com/teams/fifa16_19/?page=2&type=1",
        "https://www.fifaindex.com/teams/fifa17_75/?type=1",
        "https://www.fifaindex.com/teams/fifa17_75/?page=2&type=1",
        "https://www.fifaindex.com/teams/fifa18_278/?type=1",
        "https://www.fifaindex.com/teams/fifa18_278/?page=2&type=1"]


team_powers = pd.DataFrame(columns = ['rank_date','country_full','att', 'mid', 'def', 'ovr'])

def web_table_to_dataframe(df, urls):
    #Convert the tables in URL to dataframe
    for url in urls:
        year = int(url[36]) * 10 + int(url[37]) + 2000 #Calculate game's year.
        
        r = requests.get(url)
        html = r.text
        soup = BeautifulSoup(html)
        table = soup.find('table', {"class": "table table-striped table-teams"})
        rows = table.find_all('tr')
        
        data = []
        for row in rows[1:]:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])
            if len(cols) != 8: #Some rows of table are empty in website.
                continue
            else:
                df = df.append({'rank_date':year,'country_full':cols[1], 'att':cols[3], 'mid':cols[4], 'def':cols[5], 'ovr':cols[6]}, 
                                    ignore_index = True)
                
    #Make changes to country names to standardize the data we work with..
    df['country_full'].replace(['Holland','Rep. Of Korea','United States'], ['Netherlands','Korea Republic', 'USA'], inplace=True)
    df['country_full'] = df['country_full'].str.lower()
    return df
            
team_powers = web_table_to_dataframe(team_powers, urls)

#Dataset containing FIFA ranking of national teams from 1992-2021
#https://www.kaggle.com/tadhgfitzgerald/fifa-international-soccer-mens-ranking-1993now
team_ranks = pd.read_csv(DATADIR + 'codes/prediction/fifa_ranking.csv')
team_ranks = team_ranks[['rank', 'country_full', 'rank_date']]
team_ranks = team_ranks[(team_ranks['rank_date'] > '2005-10') & (team_ranks['rank_date'] < '2018-10')].reset_index(drop=True) #Only look at rankings from 2005-2018.
team_ranks = team_ranks[team_ranks['rank_date'].str[5:7] == '10'] # Only look at the ranks in October of each year
team_ranks['rank_date'] = team_ranks['rank_date'].str[:4].astype(int) #Only take year
team_ranks['country_full'] = team_ranks['country_full'].str.lower() # Convert letters to lowercase to standardize the data.

#Combine the strengths of the teams and their ranking by years.
team_rank_power = pd.merge(team_powers,team_ranks,on=['country_full', 'rank_date'],how='inner')
team_rank_power.rename(columns={'rank_date': 'date', 'country_full': 'name'}, inplace=True)
df = team_rank_power

# Dataset containing the results of all matches played between 1872-2017
# https://www.kaggle.com/martj42/international-football-results-from-1872-to-2017
results = pd.read_csv(DATADIR + 'codes/prediction/results.csv')
results = results.drop(['city', 'tournament', 'country'], axis=1)
results = results[(results['date'] > '2005-10') & (results['date'] < '2018-10')].reset_index(drop=True) # Only look at rankings from 2005-2018.
results['date'] = results['date'].str[:4].astype(int) # Only take year.
results['home_team'] = results['home_team'].str.lower() # We convert letters to lowercase to standardize the data.
results['away_team'] = results['away_team'].str.lower()

unique_team_names = list(team_powers.country_full.unique()) # names of teams with power information

# Only get the match results of the teams for which we have power information..
for index, row in results.iterrows():
    if row.home_team not in unique_team_names:
        results.loc[index, 'home_team'] = None
    if row.away_team not in unique_team_names:
        results.loc[index, 'away_team'] = None
results = results.dropna()

# Split the match results into Team1 Team2 instead of home_team, away_team.
results[['att1','def1','mid1','ovr1','rank1','att2','def2','mid2','ovr2','rank2']] = np.nan
for index, row in results.iterrows():
    date = row.date
    team1 = row.home_team
    team2 = row.away_team
    try:
        results.loc[index, 'att1'] = df[df.date == date][df.name == team1]['att'].iloc[0]
        results.loc[index, 'def1'] = df[df.date == date][df.name == team1]['def'].iloc[0]
        results.loc[index, 'mid1'] = df[df.date == date][df.name == team1]['mid'].iloc[0]
        results.loc[index, 'ovr1'] = df[df.date == date][df.name == team1]['ovr'].iloc[0]
        results.loc[index, 'rank1'] = df[df.date == date][df.name == team1]['rank'].iloc[0]

        results.loc[index, 'att2'] = df[df.date == date][df.name == team2]['att'].iloc[0]
        results.loc[index, 'def2'] = df[df.date == date][df.name == team2]['def'].iloc[0]
        results.loc[index, 'mid2'] = df[df.date == date][df.name == team2]['mid'].iloc[0]
        results.loc[index, 'ovr2'] = df[df.date == date][df.name == team2]['ovr'].iloc[0]
        results.loc[index, 'rank2'] = df[df.date == date][df.name == team2]['rank'].iloc[0]
    except:
        pass
results = results.dropna()

# Add the match score and who won the match to the dataframe. 
# Remove the draw status as there are no draws in the world cup matches.
results['score'] = results.home_score - results.away_score
results = results.drop(['home_score', 'away_score', 'home_team', 'away_team'], 1)
results['winner'] = None
results['winner'][results.score > 0] = 1
results['winner'][results.score < 0] = -1
results['winner'][results.score == 0] = 0
results = results[results.winner != 0]

results[['att1','def1','mid1','ovr1','rank1','att2','def2','mid2','ovr2','rank2']] = results[['att1','def1','mid1','ovr1','rank1','att2','def2','mid2','ovr2','rank2']].astype(int)

# The dataframe is edited to contain only the differences between the two sets.
results['att'] = results['att1'] - results['att2']
results['def'] = results['def1'] - results['def2']
results['mid'] = results['mid1'] - results['mid2']
results['ovr'] = results['ovr1'] - results['ovr2']
results['rank'] = results['rank1'] - results['rank2']

# delete random winner hosts to reset the home advantage.
to_drop = results[results.winner == 1].sample(171) 
results.drop(labels=to_drop.index, axis=0, inplace=True)
results.drop(['date','neutral'], axis=1, inplace=True)
results.reset_index(inplace=True, drop=True)

#####
# Machine Learning
#####

#split dataset in features and target variable
feature_cols = ['def', 'mid', 'att', 'ovr','rank']
X = results[feature_cols] # Features
y = results.winner # Target variable
y=y.astype('int')

# split X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.33,random_state=0)

#### LOGISTIC REGRESSION ####

# import the class
from sklearn.linear_model import LogisticRegression

# instantiate the model (using the default parameters)
logreg = LogisticRegression()

# fit the model with data
logreg.fit(X_train.values,y_train.values)
y_pred=logreg.predict(X_test)

# import the metrics class
from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred)) # %70 / 70 / 71 / 72
print("Precision:",metrics.precision_score(y_test, y_pred)) # %68 / 72 / 73 / 74
print("Recall:",metrics.recall_score(y_test, y_pred)) # %73 / 70 / 73 / 73

#### RANDOM FOREST ####
#Import Random Forest Model
from sklearn.ensemble import RandomForestClassifier

#Create a Gaussian Classifier
clf=RandomForestClassifier()

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)


# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred)) # %65 / 67 / 66 / 70
print("Precision:",metrics.precision_score(y_test, y_pred)) # %63 / 68 / 69 / 71
print("Recall:",metrics.recall_score(y_test, y_pred)) # %71 / 70 / 69 / 72

#### SUPPORT VECTOR MACHINE ####
#Import svm model
from sklearn import svm
from sklearn.svm import SVC

#Create a svm Classifier
clf = svm.SVC(kernel='linear') # Linear Kernel

#Train the model using the training sets
clf.fit(X_train.values, y_train.values)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy: how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred)) # %73 / 70 / 71 / 72
print("Precision:",metrics.precision_score(y_test, y_pred)) # %74 / 72 / 73 / 74
print("Recall:",metrics.recall_score(y_test, y_pred)) # %73 / 70 / 73 / 72

### SIMULATION ###

#May 2018
wc_url = ['https://www.fifaindex.com/teams/fifa18wc_248/',
          'https://www.fifaindex.com/teams/fifa18wc_248/?page=2&type=1']

wc_team_powers = pd.DataFrame(columns = ['rank_date','country_full','att', 'mid', 'def', 'ovr'])

wc_team_powers = web_table_to_dataframe(wc_team_powers, wc_url)

wc_team_ranks = pd.read_csv(DATADIR + 'codes/prediction/fifa_ranking.csv')
wc_team_ranks = wc_team_ranks[['rank', 'country_full', 'rank_date']]
wc_team_ranks = wc_team_ranks[(wc_team_ranks['rank_date'] == '2018-05-17')].reset_index(drop=True) # May 2018
wc_team_ranks['rank_date'] = wc_team_ranks['rank_date'].str[:4].astype(int)
wc_team_ranks['country_full'] = wc_team_ranks['country_full'].str.lower()

wc_team_rank_power = pd.merge(wc_team_powers,wc_team_ranks,on=['country_full', 'rank_date'],how='inner')
wc_team_rank_power.rename(columns={'rank_date': 'date', 'country_full': 'name'}, inplace=True)
wc_team_rank_power = wc_team_rank_power.drop('date', axis=1)
wc = wc_team_rank_power

def match(wc, team1, team2, random_scale=5):
    
    match = pd.DataFrame(columns=['att1','def1','mid1','ovr1','rank1','att2','def2','mid2','ovr2','rank2'], index=[0])
    
    att1 = int(wc[wc.name == team1]['att'].iloc[0])
    def1 = int(wc[wc.name == team1]['def'].iloc[0])
    mid1 = int(wc[wc.name == team1]['mid'].iloc[0])
    ovr1 = int(wc[wc.name == team1]['ovr'].iloc[0])
    rank1 = int(wc[wc.name == team1]['rank'].iloc[0])

    att2 = int(wc[wc.name == team2]['att'].iloc[0])
    def2 = int(wc[wc.name == team2]['def'].iloc[0])
    mid2 = int(wc[wc.name == team2]['mid'].iloc[0])
    ovr2 = int(wc[wc.name == team2]['ovr'].iloc[0])
    rank2 = int(wc[wc.name == team2]['rank'].iloc[0])
    
    match['att1'] = np.random.normal(att1, scale=random_scale)
    match['def1'] = np.random.normal(def1, scale=random_scale)
    match['mid1'] = np.random.normal(mid1, scale=random_scale)
    match['ovr1'] = np.random.normal(ovr1, scale=random_scale)
    match['rank1'] = np.random.normal(rank1, scale=random_scale)

    match['att2'] = np.random.normal(att2, scale=random_scale)
    match['def2'] = np.random.normal(def2, scale=random_scale)
    match['mid2'] = np.random.normal(mid2, scale=random_scale)
    match['ovr2'] = np.random.normal(ovr2, scale=random_scale)
    match['rank2'] = np.random.normal(rank2, scale=random_scale)
    
    match['att'] = match['att1'] - match['att2']
    match['def'] = match['def1'] - match['def2']
    match['mid'] = match['mid1'] - match['mid2']
    match['ovr'] = match['ovr1'] - match['ovr2']
    match['rank'] = match['rank1'] - match['rank2']

    match = match[['att', 'def', 'mid', 'ovr', 'rank']]
    
    match_array = match.values
    
    prediction = clf.predict(match_array)
    
    winner = None
    
    if prediction == 1:
        winner = team1
    elif prediction == -1:
        winner = team2
    
    return winner
    
def simulate_matches(team1, team2, n_matches=6500):
    
    match_results = []
    for i in range(n_matches):
        match_results.append(match(wc, team1, team2, random_scale=5))
        
    team1_proba = match_results.count(team1) / len(match_results) * 100
    team2_proba = match_results.count(team2) / len(match_results) * 100
    
    print(team1, str(round(team1_proba, 2)) + '%')
    print(team2, str(round(team2_proba,2)) + '%')
    print('-------------------------')
    print()
    
    if team1_proba > team2_proba:
        overall_winner = team1
    else:
        overall_winner = team2
    
    return {'team1': team1,
            'team2': team2,
            'team1_proba': team1_proba, 
            'team2_proba': team2_proba, 
            'overall_winner': overall_winner,
            'match_results': match_results}


print('Round of 16:')

ko1 = simulate_matches('uruguay', 'portugal')['overall_winner']
ko2 = simulate_matches('france', 'argentina')['overall_winner']
ko3 = simulate_matches('brazil', 'mexico')['overall_winner']
ko4 = simulate_matches('belgium', 'japan')['overall_winner']
ko5 = simulate_matches('spain', 'russia')['overall_winner']
ko6 = simulate_matches('croatia', 'denmark')['overall_winner']
ko7 = simulate_matches('sweden', 'switzerland')['overall_winner']
ko8 = simulate_matches('colombia', 'england')['overall_winner']

print()
print('Quarter Finals:')
print()

quarters1 = simulate_matches(ko1, ko2)['overall_winner']
quarters2 = simulate_matches(ko3, ko4)['overall_winner']
quarters3 = simulate_matches(ko5, ko6)['overall_winner']
quarters4 = simulate_matches(ko7, ko8)['overall_winner']

print()
print('Semi Finals:')
print()

semifinals1 = simulate_matches(quarters1, quarters2)['overall_winner']
semifinals2 = simulate_matches(quarters3, quarters4)['overall_winner']

print()
print('Finals:')
print()

finals = simulate_matches(semifinals1, semifinals2)


### VISUALIZATION OF MODEL

### Top teams by year and average of all teams
df = df.astype({"att": int, "mid": int, 'def':int,'ovr':int})
year_dic = {}

for year in df.date.unique():
    df_year = df[df.date == year]
    df_year = df_year[df_year.ovr == df_year.ovr.max()]
    year_dic[year] = [max(df_year.ovr.tolist()), df_year.name.tolist()]

mean_ovrs = []
for year in df.date.unique():
    df_year = df[df.date == year]
    df_year['ovr'] = pd.to_numeric(df_year['ovr'])
    mean_ovrs.append(df_year.ovr.mean())


years = list(year_dic.keys())
max_ovrs = [i[0] for i in list(year_dic.values())]
teams = [i[1] for i in list(year_dic.values())]

teams_str = []
for t in teams:
    try:
        teams_str.append(str(', '.join(t)))
    except:
        teams_str.append(t)

import plotly.graph_objs as go
import plotly.io as pio
pio.renderers.default='browser'

trace1= go.Bar(
            x=years,
            y=max_ovrs,
            text=teams_str,
            name = 'Max Performance',
            marker=dict(
            color='rgb(103,113,242)')
    )

trace2 = go.Scatter(
    x = years,
    y = mean_ovrs,
    mode = 'lines+markers',
    name = 'Mean Performance',
    marker = dict(
        size = 12,
        color = 'rgba(300, 300, 300, .9)',
        line = dict(
            width = 2)
        )
)

data = [trace1, trace2]

layout = go.Layout(
    title='Powers of top teams by years',
    title_x=0.5,
    xaxis_title="Year",
    yaxis_title="Power",
    
)

team_powers_bar = go.Figure(data=data, layout=layout)
team_powers_bar.write_html("team_powers_bar.html")


### Distribution of the strengths of the teams by years
data=[]
for year in years:
    
    values = df.ovr[df.date==year].tolist()
    
    trace1 = go.Scatter(
                x=[year] * len(values),
                y=values,
                mode='markers',
                marker=dict(
                color='rgb(103,113,242)')
        )
    
    data.append(trace1)
    
layout = go.Layout(
    title='Distribution of the powers of the teams by years',
    title_x=0.5,
    xaxis_title="Year",
    yaxis_title="Power",
    
)

team_powers_scatter = go.Figure(data=data, layout=layout)
team_powers_scatter.update_traces(showlegend=False,marker_size=5)
team_powers_scatter.write_html("team_powers_scatter.html")

    
### Relationship between team strengths and total scores
trace = go.Scatter(
    x = results.ovr1,
    y = results.score,
    mode = 'markers',
    name = 'Mean Performance',
    marker = dict(
        size = 12,
        color = 'rgba(300, 300, 300, .9)',
        line = dict(
            width = 2)
        )
)

data = [trace]

layout = go.Layout(
    title='Goal Difference According to Team Power',
    title_x=0.5,
    xaxis_title="Power",
    yaxis_title="Goal Difference",
    
)

team_powers_scores = go.Figure(data=data, layout=layout)
team_powers_scores.write_html("team_powers_scores.html")

### Show of teams' strengths
trace = go.Scatter3d(
    x = results.att1,
    y = results.def1,
    z = results.mid1,
    mode = 'markers',
    name = 'Mean Performance',
    marker = dict(
        size = np.power(results.score.tolist(), 2),
        color = 'rgba(100, 150, 300, .9)',
        line = dict(
            width = 1)
        )
)

data = [trace]

layout = {
  "margin": {
    "r": 10, 
    "t": 25, 
    "b": 40, 
    "l": 60
  }, 
  "paper_bgcolor": "rgb(243, 243, 243)", 
  "plot_bgcolor": "rgb(243, 243, 243)", 
  "scene": {
    "xaxis": {
      "gridcolor": "rgb(255, 255, 255)", 
      "gridwidth": 2, 
      "ticklen": 5, 
      "title": "Attack", 
      "type": "log", 
      "zerolinewidth": 1
    }, 
    "yaxis": {
      "gridcolor": "rgb(255, 255, 255)", 
      "ticklen": 5, 
      "title": "Defense", 
      "zerolinewidth": 1
    }, 
    "zaxis": {
      "gridcolor": "rgb(255, 255, 255)", 
      "ticklen": 5, 
      "title": "Midside", 
      "type": "log", 
      "zerolinewidth": 1
    }
  }, 
  "title": "Teams Performance 3D", 
  "title_x" :0.5,
  "xaxis": {"domain": [0, 1]}, 
  "yaxis": {"domain": [0, 1]}
}
team_powers_3d = go.Figure(data=data, layout=layout)
team_powers_3d.write_html("team_powers_3d.html")

# After how many attempts is a stable result obtained?
simulation_test = simulate_matches('croatia', 'denmark', n_matches=10000)

p_list = []
for i in range(len(simulation_test['match_results'])):
    denmark = simulation_test['match_results'][:i].count('denmark') / (i+1) * 100
    croatia = simulation_test['match_results'][:i].count('croatia') / (i+1) * 100
    p_list.append(denmark - croatia)
trace = go.Scatter( y = p_list,
                    name='Teams divergence by number of simulations',
                    marker= dict(color='rgb(230,90,110)')
                    )

data = [trace]
number_of_simulastions_viz = go.Figure(data=data)
number_of_simulastions_viz.update_layout(title='How many trials required for consistent results?', 
                                         title_x=0.5,
                                         xaxis_title="Number of Simulations",
                                         yaxis_title="Consistency",
                  )
number_of_simulastions_viz.write_html("number_of_simulastions_viz.html")

## Compare models
from sklearn import model_selection

X = results[feature_cols] # Features
Y = results.winner # Target variable
Y=Y.astype('int')

outcome = []
model_names = []
models = [('LogReg', LogisticRegression()), 
          ('SVM', SVC()), 
          ('RFC', RandomForestClassifier())]

for model_name, model in models:
    k_fold_validation = model_selection.KFold(n_splits=10)
    results = model_selection.cross_val_score(model, X, Y, cv=k_fold_validation, scoring='accuracy')
    outcome.append(results)
    model_names.append(model_name)
    output_message = "%s| Mean=%f STD=%f" % (model_name, results.mean(), results.std())

compare_models_viz = go.Figure()
compare_models_viz.add_trace(go.Box(y=outcome[0], name="Logistic Regression"))
compare_models_viz.add_trace(go.Box(y=outcome[1], name="Support Vector Machine"))
compare_models_viz.add_trace(go.Box(y=outcome[2], name="Random Forest Classifier"))
compare_models_viz.update_layout(
    yaxis_title="Models' Scores",
    title="Model Comparison",
    title_x=0.5,
)

compare_models_viz.write_html("compare_models_viz.html")