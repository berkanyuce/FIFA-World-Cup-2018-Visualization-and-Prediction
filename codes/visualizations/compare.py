import matplotlib.pyplot as plt
import streamlit as st
from mplsoccer import VerticalPitch
from utilites.data_loading import choosed_match_dataframe
from utilites.utility_functions import nums_cumulative_sum

def xg_viz(home_team, away_team,event_type):
    #shows xg graph using by shots
    st.set_option('deprecation.showPyplotGlobalUse', False)

    df = choosed_match_dataframe(home_team,away_team,event_type)
    shots = df.loc[df['type'] == 'Shot'].set_index('id')
    shots = shots[shots['period'] < 5]


    a_xG = [0] #away xg
    h_xG = [0] #home xg
    a_min = [0] #away shot minute
    h_min = [0] #home shot minute
    
    #Plot graph using by statsbomb's xg values
    for x in range(len(shots['shot_statsbomb_xg'])):
        if shots['team'][x] == away_team:
            a_xG.append(shots['shot_statsbomb_xg'][x])
            a_min.append(shots['minute'][x])
        if shots['team'][x] == home_team:
            h_xG.append(shots['shot_statsbomb_xg'][x])
            h_min.append(shots['minute'][x])
            
        #add xg values as cumulative
        a_cumulative = nums_cumulative_sum(a_xG)
        h_cumulative = nums_cumulative_sum(h_xG)
                
        #Plot xg graph
        fig, ax = plt.subplots(figsize = (10, 5))
        fig.set_facecolor('white')
        ax.patch.set_facecolor('white')
        
        plt.xticks([0, 15, 30, 45, 60, 75, 90])
        plt.xlabel('Minute')
        plt.ylabel('xG')
        
        ax.step(x=a_min, y=a_cumulative, where='post', label=home_team)
        ax.step(x=h_min, y=h_cumulative, where='post', label=away_team)
        ax.legend()

def xg_shots(non_goals, goals):
    #Plot all shots using by their xG values.
    
    pitch = VerticalPitch(pitch_type='statsbomb', line_color='#000009', half=True,pad_top=0.5,  # only a small amount of space at the top of the pitch
                      pad_bottom=-20,  # reduce the area displayed at the bottom of the pitch
                      pad_left=-15,  # reduce the area displayed on the left of the pitch
                      pad_right=-15,  # reduce the area displayed on the right of the pitch
                      goal_type='line')

    fig, ax = pitch.draw(figsize=(12, 10))
    
    pitch.scatter(non_goals.x, non_goals.y,
                    # size varies between 100 and 1900 (points squared)
                    s=(non_goals.shot_statsbomb_xg * 1900) + 100,
                    edgecolors='#606060',  # give the markers a charcoal border
                    c='None',  # no facecolor for the markers
                    hatch='///',  # the all important hatch (triple diagonal lines)
                    # for other markers types see: https://matplotlib.org/api/markers_api.html
                    marker='o',
                    ax=ax)
    
    # plot goal shots with a color
    pitch.scatter(goals.x, goals.y,
                    # size varies between 100 and 1900 (points squared)
                    s=(goals.shot_statsbomb_xg * 1900) + 100,
                    edgecolors='#606060',  # give the markers a charcoal border
                    c='#b94b75',  # color for scatter in hex format
                    # for other markers types see: https://matplotlib.org/api/markers_api.html
                    marker='o',
                    ax=ax)