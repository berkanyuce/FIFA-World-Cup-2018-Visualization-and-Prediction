import streamlit as st

from utilites.dictionary import my_dictionary as dct
import header.visualization as vz
from utilites.data_loading import match_results,teams
from utilites.groups import (
group_a_matches,group_b_matches,group_c_matches,
group_d_matches,group_e_matches,group_f_matches,
group_g_matches,group_h_matches)

st.set_page_config(layout="wide")

def show_x_finals(matches, row, s, f, event_type):
    choosed_match =  st.sidebar.selectbox(dct['Select Match'], matches[row][s:f]) #Select a avalaible match 
    choosed_match = matches.index[matches[row] == choosed_match][0] #Get match by given row value
    home_team = matches[dct['home_team']][choosed_match] #Get home team name
    away_team = matches[dct['away_team']][choosed_match] #Get away team name
    vz.show_match_viz(event_type, home_team, away_team, choosed_match) #Call a function from visualization.py    
    
def show_group_matches(group1_matches, match_results):
    choosed_match = st.sidebar.selectbox(dct['Select Match'], group1_matches[:,3])
    choosed_match = match_results.index[match_results[dct['Full_Match_Info']] == choosed_match][0]
    st.write(match_results[dct['Full_Match_Info']][choosed_match])

#We have 3 analyze type
choosed_analyze = st.sidebar.selectbox(dct['Select Analyze Type'], [dct['Match Analyze'],dct['Team Analyze'], dct['Player Analyze']])

#Appropriate match information is called according to the selected analysis type and match.
if choosed_analyze == dct['Match Analyze']:
    choosed_event = st.sidebar.selectbox(dct['Select Event Type'], [dct['Final'],dct['Third Place'], dct['Semi Finals'], dct['Quarter Finals'], dct['Round of 16'], dct['Group Stage']])
    
    #Final match's id is '1' and the others placed between numbers.
    #Group matches' methods are different
    if choosed_event == dct['Final']:
        show_x_finals(match_results, dct['Full_Match_Info'], 1, 2, choosed_event)
    elif choosed_event == dct['Third Place']:
        show_x_finals(match_results, dct['Full_Match_Info'], 0, 1, choosed_event)
    elif choosed_event == dct['Semi Finals']:
        show_x_finals(match_results, dct['Full_Match_Info'], 62, 64, choosed_event)
    elif choosed_event == dct['Quarter Finals']:
        show_x_finals(match_results, dct['Full_Match_Info'], 50, 54, choosed_event)
    elif choosed_event == dct['Round of 16']:
        show_x_finals(match_results, dct['Full_Match_Info'], 54, 62, choosed_event)
    elif choosed_event == dct['Group Stage']:
        choosed_group = st.sidebar.selectbox(dct['Select Group'], [dct['Group A'],dct['Group B'],dct['Group C'],dct['Group D'],
                                                              dct['Group E'],dct['Group F'],dct['Group G'],dct['Group H']])
        choosed_group = choosed_group[-1:]
        if choosed_group == dct['A']:
            show_group_matches(group_a_matches, match_results)
        elif choosed_group == dct['B']:
            show_group_matches(group_b_matches, match_results)
        elif choosed_group == dct['C']:
            show_group_matches(group_c_matches, match_results)
        elif choosed_group == dct['D']:
            show_group_matches(group_d_matches, match_results)
        elif choosed_group == dct['E']:
            show_group_matches(group_e_matches, match_results)
        elif choosed_group == dct['F']:
            show_group_matches(group_f_matches, match_results)
        elif choosed_group == dct['G']:
            show_group_matches(group_g_matches, match_results)
        else:
            show_group_matches(group_h_matches, match_results)

elif choosed_analyze == dct['Team Analyze']:
    choosed_event = st.sidebar.selectbox(dct['Select Team'], teams[:])
    

