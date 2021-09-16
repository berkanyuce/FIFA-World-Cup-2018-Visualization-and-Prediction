import pandas as pd
from statsbombpy import sb
from utilites.utilites import add_locations
from utilites.dictionary import my_dictionary as dct

DATADIR = 'https://raw.githubusercontent.com/berkanyuce/FIFA-World-Cup-2018-Visualization/main/'
groups = pd.read_csv(DATADIR+'data/csv/Groups.csv',parse_dates=[0])
img = DATADIR + '/data/images/TeamLogos/' #Team logos' directory

competitions = sb.competitions() #Get competitions from Statsbomb 
matches = sb.matches(competition_id=43, season_id=3) #Get world cup matches from Statsbomb

#Event DataFrame
def event_dataframe():
    competition_stage = 'Final'; home_team = 'France'; away_team = 'Croatia'
    
    match = matches[matches[dct['away_team']] == away_team]
    match = match[match[dct['home_team']] == home_team]
    match = match[match[dct['competition_stage']] == competition_stage]
    match.reset_index(drop=True, inplace=True)
    
    match_id = match[dct['match_id']][0] 
        
    df = sb.events(match_id=match_id)
     
    #add playerid column
    player_id = []
    lineup = sb.lineups(match_id=match_id) 
    for i in range(len(df[dct['player']])):
        if type(df[dct['player']][i]) == float:
            player_id.append(float(dct['nan']))
        else:
            if df[dct['team']][i] == home_team:
                player_id.append(lineup[home_team][lineup[home_team][dct['player_name']] == df[dct['player']][i]][dct['player_id']].reset_index(drop=True)[0])
            else:
                player_id.append(lineup[away_team][lineup[away_team][dct['player_name']] == df[dct['player']][i]][dct['player_id']].reset_index(drop=True)[0])
    df[dct['player_id']] = player_id
    
    #add pass_recipient_id column
    pass_recipient_id = []
    for i in range(len(df[dct['pass_recipient']])):
        if type(df[dct['pass_recipient']][i]) == float:
            pass_recipient_id.append(float(dct['nan']))
        else:
            if df[dct['team']][i] == home_team:
                pass_recipient_id.append(lineup[home_team][lineup[home_team][dct['player_name']] == df[dct['pass_recipient']][i]][dct['player_id']].reset_index(drop=True)[0])
            else:
                pass_recipient_id.append(lineup[away_team][lineup[away_team][dct['player_name']] == df[dct['pass_recipient']][i]][dct['player_id']].reset_index(drop=True)[0])
    df[dct['pass_recipient_id']] = pass_recipient_id
       
    return df

df = event_dataframe()

#match results
match_results = matches[[dct['competition_stage'], dct['home_team'], dct['home_score'], dct['away_score'], dct['away_team']]]
match_results[dct['Score']] = match_results[dct['home_score']].astype(str) + '-' + match_results[dct['away_score']].astype(str)
match_results[dct['Full_Match_Info']] = match_results[dct['home_team']] + ' ' + match_results[dct['Score']] + ' ' + match_results[dct['away_team']]
match_results.sort_values(dct['competition_stage'], inplace=True)
match_results.reset_index(drop=True, inplace=True)

#group matches
group_matches = match_results[match_results[dct['competition_stage']] == dct['Group Stage']]
group_matches.reset_index(drop=True, inplace=True)

#teams
teams = pd.concat([matches[dct['home_team']], matches[dct['away_team']]], axis=0)
teams.drop_duplicates(inplace=True)
teams.reset_index(drop=True, inplace=True)

######

home_team = df[dct['team']][0]
away_team = df[dct['team']][1]

home_event = df[df[dct['team']] == home_team]
away_event = df[df[dct['team']] == away_team]

all_passes = df[df[dct['type']] == dct['Pass']]
home_passes = all_passes[all_passes[dct['team']]==home_team]
away_passes = all_passes[all_passes[dct['team']]==away_team]

shots = df.loc[df[dct['type']] == dct['Shot']].set_index(dct['id'])
home_shots = shots.loc[shots[dct['possession_team']] == home_team]
away_shots = shots.loc[shots[dct['possession_team']] == away_team]

goals = df.loc[df[dct['shot_outcome']] == dct['Goal']].set_index(dct['id'])
own_goals = df.loc[df[dct['type']] == dct['Own Goal Against']].set_index(dct['id'])
goals = [goals, own_goals]; goals = pd.concat(goals); goals.sort_values(by=dct['minute'], inplace=True)
home_goals = goals.loc[goals[dct['possession_team']] == home_team][[dct['team'], dct['player'], dct['minute'], dct['location'], dct['shot_statsbomb_xg']]].replace([away_team,home_team], [dct['(OG)'], ' '])
away_goals = goals.loc[goals[dct['possession_team']] == away_team][[dct['team'], dct['player'], dct['minute'], dct['location'], dct['shot_statsbomb_xg']]].replace([home_team,away_team], [dct['(OG)'], ' '])
home_goals = add_locations(home_goals)
away_goals = add_locations(away_goals)

non_goals = shots.loc[shots[dct['shot_outcome']] != dct['Goal']]
home_non_goals = non_goals.loc[non_goals[dct['possession_team']] == home_team]
away_non_goals = non_goals.loc[non_goals[dct['possession_team']] == away_team]
home_non_goals = add_locations(home_non_goals)
away_non_goals = add_locations(away_non_goals)
