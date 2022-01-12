from utilites.utility_functions import Pitch_class
from utilites.data_loading import choosed_match_dataframe
from utilites.dictionary import my_dictionary as dct
import pandas as pd
import matplotlib.pyplot as plt

def show_lineup_viz(home_team,away_team,event_type):
    df = choosed_match_dataframe(home_team,away_team,event_type)
    #get lineup position ids
    home_position_id = []
    away_position_id = []
    
    #Add jersey numbers to lineup df
    home_jersey_number = []
    away_jersey_number = []
    
    #Add player names to lineup df
    home_player_name = []
    away_player_name = []
    
    for i in range(len(df['tactics'][0]['lineup'])):
        home_position_id.append(df['tactics'][0]['lineup'][i]['position']['id'])
        away_position_id.append(df['tactics'][1]['lineup'][i]['position']['id'])
        
        home_jersey_number.append(df['tactics'][0]['lineup'][i]['jersey_number'])
        away_jersey_number.append(df['tactics'][1]['lineup'][i]['jersey_number'])
    
        home_player_name.append(df.tactics[0]['lineup'][i]['player']['name'])
        away_player_name.append(df.tactics[1]['lineup'][i]['player']['name'])
    
    #Add position's x and y values
    home_position_x = []
    home_position_y = []
    away_position_x = []
    away_position_y = []
    for i in range(11):
        home_position_x.append(dct.get(home_position_id[i]).get('x') / 2)
        home_position_y.append(dct.get(home_position_id[i]).get('y'))
        away_position_x.append(120 - (dct.get(away_position_id[i]).get('x') / 2))
        away_position_y.append(dct.get(away_position_id[i]).get('y'))
        
    #Merges all lineup infos into home/away_lineup
    home_lineup = pd.DataFrame(list(zip(home_position_id, home_player_name, home_position_x, home_position_y, home_jersey_number)),
                   columns =['position_id', 'player_name', 'position_x', 'position_y', 'jersey_number'])
    away_lineup = pd.DataFrame(list(zip(away_position_id, away_player_name, away_position_x, away_position_y, away_jersey_number)),
                   columns =['position_id', 'player_name', 'position_x', 'position_y', 'jersey_number'])
    
    #Create a pitch by using create_pitch.py
    pitch = Pitch_class()
    pitch, fig, ax = pitch.create_pitch()
    
    #Plotting dots
    plt.scatter(home_lineup['position_x'], home_lineup['position_y'], color='black', s=700)
    plt.scatter(away_lineup['position_x'], away_lineup['position_y'], color='red', s=700)
    
    #Plotting player names and jersey numbers
    for index, row in home_lineup.iterrows():
        pitch.annotate(int(row.jersey_number), xy=(row.position_x, row.position_y), c='white', va='center',
                       ha='center', size=15, ax=ax)
        pitch.annotate(row.player_name, xy=(row.position_x, row.position_y-3), c='black', va='center',
                       ha='center', size=15, ax=ax)
    for index, row in away_lineup.iterrows():
        pitch.annotate(int(row.jersey_number), xy=(row.position_x, row.position_y), c='white', va='center',
                       ha='center', size=15, ax=ax)
        pitch.annotate(row.player_name, xy=(row.position_x, row.position_y-3), c='black', va='center',
                       ha='center', size=15, ax=ax)