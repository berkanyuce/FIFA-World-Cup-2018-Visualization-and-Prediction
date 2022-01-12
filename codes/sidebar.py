import streamlit as st

import header.visualization as vz
from utilites.data_loading import match_results
from utilites.groups import (
group_a_matches,group_b_matches,group_c_matches,
group_d_matches,group_e_matches,group_f_matches,
group_g_matches,group_h_matches)
from prediction.prediction_report import prediction_report

st.set_page_config(layout="wide")

def show_x_finals(matches, row, s, f, event_type):
    choosed_match =  st.sidebar.selectbox('Select Match', matches[row][s:f]) #Select a avalaible match 
    choosed_match = matches.index[matches[row] == choosed_match][0] #Get match by given row value
    home_team = matches['home_team'][choosed_match] #Get home team name
    away_team = matches['away_team'][choosed_match] #Get away team name
    vz.show_match_viz(event_type, home_team, away_team, choosed_match) #Call a function from visualization.py    
    
def show_group_matches(group1_matches, match_results):
    choosed_match = st.sidebar.selectbox('Select Match', group1_matches['Full_Match_Info'][:])
    choosed_match = match_results.index[match_results['Full_Match_Info'] == choosed_match][0]
    event_type = 'Group Stage'
    home_team = match_results['home_team'][choosed_match] #Get home team name
    away_team = match_results['away_team'][choosed_match] #Get away team name
    vz.show_match_viz(event_type, home_team, away_team, choosed_match) #Call a function from visualization.py    

#We have 3 analyze type
choosed_analyze = st.sidebar.selectbox('Select Analyze Type', ['Match Analyze', 'Tournament Prediction'])

#Appropriate match information is called according to the selected analysis type and match.
if choosed_analyze == 'Match Analyze':
    choosed_event = st.sidebar.selectbox('Select Event Type', ['Final','Third Place', 'Semi Finals', 'Quarter Finals', 'Round of 16', 'Group Stage'])
    
    #Final match's id is '1' and the others placed between numbers.
    #Group matches' methods are different
    if choosed_event == 'Final':
        show_x_finals(match_results, 'Full_Match_Info', 1, 2, 'Final')
    elif choosed_event == 'Third Place':
        show_x_finals(match_results, 'Full_Match_Info', 0, 1, '3rd Place Final')
    elif choosed_event == 'Semi Finals':
        show_x_finals(match_results, 'Full_Match_Info', 62, 64, 'Semi-finals')
    elif choosed_event == 'Quarter Finals':
        show_x_finals(match_results, 'Full_Match_Info', 50, 54, 'Quarter-finals')
    elif choosed_event == 'Round of 16':
        show_x_finals(match_results, 'Full_Match_Info', 54, 62, 'Round of 16')
    elif choosed_event == 'Group Stage':
        choosed_group = st.sidebar.selectbox('Select Group', ['Group A','Group B','Group C','Group D',
                                                              'Group E','Group F','Group G','Group H'])
        choosed_group = choosed_group[-1:]
        if choosed_group == 'A':
            show_group_matches(group_a_matches, match_results)
        elif choosed_group == 'B':
            show_group_matches(group_b_matches, match_results)
        elif choosed_group == 'C':
            show_group_matches(group_c_matches, match_results)
        elif choosed_group == 'D':
            show_group_matches(group_d_matches, match_results)
        elif choosed_group == 'E':
            show_group_matches(group_e_matches, match_results)
        elif choosed_group == 'F':
            show_group_matches(group_f_matches, match_results)
        elif choosed_group == 'G':
            show_group_matches(group_g_matches, match_results)
        else:
            show_group_matches(group_h_matches, match_results)

elif choosed_analyze == 'Tournament Prediction':
    prediction_report()