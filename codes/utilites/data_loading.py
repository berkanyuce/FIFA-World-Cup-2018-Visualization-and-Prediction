import pandas as pd
from statsbombpy import sb

DATADIR = 'https://raw.githubusercontent.com/berkanyuce/FIFA-World-Cup-2018-Visualization/main/'
groups = pd.read_csv(DATADIR+'data/csv/Groups.csv',parse_dates=[0])
img = DATADIR + '/data/images/TeamLogos/' #Team logos' directory

competitions = sb.competitions() #Get competitions from Statsbomb 
matches = sb.matches(competition_id=43, season_id=3) #Get world cup matches from Statsbomb

#match results
match_results = matches[['competition_stage', 'home_team', 'home_score', 'away_score', 'away_team']]
match_results['Score'] = match_results['home_score'].astype(str) + '-' + match_results['away_score'].astype(str)
match_results['Full_Match_Info'] = match_results['home_team'] + ' ' + match_results['Score'] + ' ' + match_results['away_team']
match_results.sort_values('competition_stage', inplace=True)
match_results.reset_index(drop=True, inplace=True)

#group matches
group_matches = match_results[match_results['competition_stage'] == 'Group Stage']
group_matches.reset_index(inplace=True)
group_matches = pd.merge(group_matches,groups, how='left', left_on='home_team', right_on='Team')

#teams
teams = pd.concat([matches['home_team'], matches['away_team']], axis=0)
teams.drop_duplicates(inplace=True)
teams.reset_index(drop=True, inplace=True)

def choosed_match_dataframe(home_team,away_team,event_type):
    match = matches[matches['away_team'] == away_team]
    match = match[match['home_team'] == home_team]
    match = match[match['competition_stage'] == event_type]
    match.reset_index(drop=True, inplace=True)
    
    match_id = match['match_id'][0] 
        
    df = sb.events(match_id=match_id)
     
    #add playerid column
    player_id = []
    lineup = sb.lineups(match_id=match_id) 
    for i in range(len(df['player'])):
        if type(df['player'][i]) == float:
            player_id.append(float('nan'))
        else:
            if df['team'][i] == home_team:
                player_id.append(lineup[home_team][lineup[home_team]['player_name'] == df['player'][i]]['player_id'].reset_index(drop=True)[0])
            else:
                player_id.append(lineup[away_team][lineup[away_team]['player_name'] == df['player'][i]]['player_id'].reset_index(drop=True)[0])
    df['player_id'] = player_id
    
    #add pass_recipient_id column
    pass_recipient_id = []
    for i in range(len(df['pass_recipient'])):
        if type(df['pass_recipient'][i]) == float:
            pass_recipient_id.append(float('nan'))
        else:
            if df['team'][i] == home_team:
                pass_recipient_id.append(lineup[home_team][lineup[home_team]['player_name'] == df['pass_recipient'][i]]['player_id'].reset_index(drop=True)[0])
            else:
                pass_recipient_id.append(lineup[away_team][lineup[away_team]['player_name'] == df['pass_recipient'][i]]['player_id'].reset_index(drop=True)[0])
    df['pass_recipient_id'] = pass_recipient_id
       
    return df
