import pandas as pd
import streamlit as st
from utilites.utility_functions import Pitch_class, add_locations
from utilites.data_loading import choosed_match_dataframe

def pass_network(passes, event):
    #Plotting pass network visualization
    
    #sperate locations from [x,y] to x column y column
    passes = add_locations(passes)
    
    #Unsuccessfull passes have unsuccessfull info. But success passes don't. So, fill nan values.
    passes['pass_outcome'].fillna('Success', inplace=True)
    passes_success = passes[passes['pass_outcome'] == 'Success']
    
    #We create pass network until first substitution.
    subs = event[event['type'] == 'Substitution']
    subs = subs['minute']
    first_sub = subs.min()
    
    passes_success = passes[passes['minute'] < first_sub]     #get all passes until first substitution
    pas = pd.to_numeric(passes_success['player_id'], downcast='integer') #Passer id
    rec = pd.to_numeric(passes_success['pass_recipient_id'], downcast='integer') #Pass recipient id
    passes_success['player_id'] = pas #success passers
    passes_success['pass_recipient_id'] = rec #success pass recipients
    average_locations = passes_success.groupby('player_id').agg({'x' : ['mean'], 'y':['mean', 'count']}) #SQL code. Groups players by mean(x) and mean(y)
    average_locations.columns = ['x', 'y', 'count']
    pass_between = passes_success.groupby(['player_id', 'pass_recipient_id']).id.count().reset_index() #SQL code. Groups passers and recipients
    pass_between.rename({'id':'pass_count'}, axis='columns', inplace=True)
    pass_between = pass_between.merge(average_locations, left_on='player_id', right_index=True)
    pass_between = pass_between.merge(average_locations, left_on='pass_recipient_id', right_index=True, suffixes=['', '_end'])
    pass_between = pass_between[pass_between['pass_count'] > 3]
    
    return pass_between, average_locations

def plot_pn_viz(pass_between, average_locations):
    pitch = Pitch_class()
    pitch, fig, ax = pitch.create_pitch()
    pitch.arrows(1.2*pass_between.x, .8*pass_between.y, 1.2*pass_between.x_end, .8*pass_between.y_end, ax=ax,
                      width = 3, headwidth = 3, color='black', zorder=1, alpha = .5)

    pitch.scatter(1.2*average_locations.x, .8*average_locations.y, s = 300, color = '#d3d3d3', edgecolors = 'black',
                     linewidth = 2.5, alpha = 1, zorder = 1, ax=ax)

def pn_main(home_team,away_team,event_type):
    col1,col2 = st.columns(2)

    df = choosed_match_dataframe(home_team,away_team,event_type)
    home_event = df[df['team'] == home_team]
    away_event = df[df['team'] == away_team]
    
    all_passes = df[df['type'] == 'Pass']
    home_passes = all_passes[all_passes['team']==home_team]
    away_passes = all_passes[all_passes['team']==away_team]

    home_pass_between, home_average_locations = pass_network(home_passes, home_event) #gets home passes and average locations
    col1.pyplot(plot_pn_viz(home_pass_between, home_average_locations)) #Plots
   
    away_pass_between, away_average_locations = pass_network(away_passes, away_event)
    col2.pyplot(plot_pn_viz(away_pass_between, away_average_locations))