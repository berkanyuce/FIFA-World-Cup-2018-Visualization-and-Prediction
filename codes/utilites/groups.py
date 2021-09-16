import numpy as np
import streamlit as st
from utilites.data_loading import groups, group_matches
from utilites.dictionary import my_dictionary as dct

def group_x_matches(matches, groups):
    group_a_matches = [];    group_b_matches = [];
    group_c_matches = [];    group_d_matches = [];
    group_e_matches = [];    group_f_matches = [];
    group_g_matches = [];    group_h_matches = [];

    for i in range(len(groups[dct['Team']])):
        team = groups[dct['Team']][i]
        for j in range(len(matches[dct['home_team']])):
            if matches[dct['home_team']][j] == team :
                group_name = groups[dct['Group Name']][i]
                
                if group_name == dct['A']:
                    group_a_matches.append(matches.iloc[j])
                elif group_name == dct['B']:
                    group_b_matches.append(matches.iloc[j])
                elif group_name == dct['C']:
                    group_c_matches.append(matches.iloc[j])
                elif group_name == dct['D']:
                    group_d_matches.append(matches.iloc[j])
                elif group_name == dct['E']:
                    group_e_matches.append(matches.iloc[j])
                elif group_name == dct['F']:
                    group_f_matches.append(matches.iloc[j])
                elif group_name == dct['G']:
                    group_g_matches.append(matches.iloc[j])
                else:
                    group_h_matches.append(matches.iloc[j])
    group_a_matches = group_x_matches_converted(group_a_matches);group_b_matches = group_x_matches_converted(group_b_matches);
    group_c_matches = group_x_matches_converted(group_c_matches);group_f_matches = group_x_matches_converted(group_f_matches);
    group_d_matches = group_x_matches_converted(group_d_matches);group_g_matches = group_x_matches_converted(group_g_matches);
    group_e_matches = group_x_matches_converted(group_e_matches);group_h_matches = group_x_matches_converted(group_h_matches);
    
    return group_a_matches,group_b_matches,group_c_matches,group_d_matches,group_e_matches,group_f_matches,group_g_matches,group_h_matches
        
def group_x_matches_converted(matches):
    m = np.array([[0,0,0,0]])
    for i in range(len(matches)):
        a = np.array([[matches[i][dct['home_team']], 
                       str(matches[i][dct['home_score']])+ '-' +str(matches[i][dct['away_score']]),
                       matches[i][dct['away_team']], 
                       matches[i][dct['home_team']]+' '+ matches[i][dct['Score']] +' ' +matches[i][dct['away_team']]]])
        m = np.append(m, a, axis = 0)
    m = np.delete(m, 0, 0)
    return m

def plot_groups(groups, group_a_matches,group_b_matches,group_c_matches,group_d_matches,group_e_matches,group_f_matches,group_g_matches,group_h_matches):
    col1, col2 = st.beta_columns(2)
    col1.write(groups[0:4],use_column_width=True);col2.write(group_a_matches,use_column_width=True)
    col1.write(groups[4:8],use_column_width=True);col2.write(group_b_matches,use_column_width=True)
    col1.write(groups[8:12],use_column_width=True);col2.write(group_c_matches,use_column_width=True)
    col1.write(groups[12:16],use_column_width=True);col2.write(group_d_matches,use_column_width=True)
    col1.write(groups[16:20],use_column_width=True);col2.write(group_e_matches,use_column_width=True)
    col1.write(groups[20:24],use_column_width=True);col2.write(group_f_matches,use_column_width=True)
    col1.write(groups[24:28],use_column_width=True);col2.write(group_g_matches,use_column_width=True)
    col1.write(groups[28:32],use_column_width=True);col2.write(group_h_matches,use_column_width=True)



group_a_matches,group_b_matches,group_c_matches,group_d_matches,group_e_matches,group_f_matches,group_g_matches,group_h_matches = group_x_matches(group_matches, groups)

#plot_groups(groups, group_a_matches,group_b_matches,group_c_matches,group_d_matches,group_e_matches,group_f_matches,group_g_matches,group_h_matches)





    
    
    
