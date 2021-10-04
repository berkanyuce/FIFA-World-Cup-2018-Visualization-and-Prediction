import pandas as pd
from statsbombpy import sb
from utilites.dictionary import my_dictionary as dct

DATADIR = 'https://raw.githubusercontent.com/berkanyuce/FIFA-World-Cup-2018-Visualization/main/'
groups = pd.read_csv(DATADIR+'data/csv/Groups.csv',parse_dates=[0])
img = DATADIR + '/data/images/TeamLogos/' #Team logos' directory

competitions = sb.competitions() #Get competitions from Statsbomb 
matches = sb.matches(competition_id=43, season_id=3) #Get world cup matches from Statsbomb

#match results
match_results = matches[[dct['competition_stage'], dct['home_team'], dct['home_score'], dct['away_score'], dct['away_team']]]
match_results[dct['Score']] = match_results[dct['home_score']].astype(str) + '-' + match_results[dct['away_score']].astype(str)
match_results[dct['Full_Match_Info']] = match_results[dct['home_team']] + ' ' + match_results[dct['Score']] + ' ' + match_results[dct['away_team']]
match_results.sort_values(dct['competition_stage'], inplace=True)
match_results.reset_index(drop=True, inplace=True)

#group matches
group_matches = match_results[match_results[dct['competition_stage']] == dct['Group Stage']]
group_matches.reset_index(inplace=True)
group_matches = pd.merge(group_matches,groups, how='left', left_on='home_team', right_on='Team')

#teams
teams = pd.concat([matches[dct['home_team']], matches[dct['away_team']]], axis=0)
teams.drop_duplicates(inplace=True)
teams.reset_index(drop=True, inplace=True)

def choosed_match_dataframe(home_team,away_team,event_type):
    match = matches[matches[dct['away_team']] == away_team]
    match = match[match[dct['home_team']] == home_team]
    match = match[match[dct['competition_stage']] == event_type]
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