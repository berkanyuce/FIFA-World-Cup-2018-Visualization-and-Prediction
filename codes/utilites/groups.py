import streamlit as st
from utilites.data_loading import groups, group_matches
from utilites.dictionary import my_dictionary as dct

def group_x_matches(group_matches, groups):
    group_a_matches = [];    group_b_matches = [];
    group_c_matches = [];    group_d_matches = [];
    group_e_matches = [];    group_f_matches = [];
    group_g_matches = [];    group_h_matches = [];

    group_matches = group_matches.groupby('Group Name')
    group_a_matches = group_matches.get_group('A').reset_index(drop=True)
    group_b_matches = group_matches.get_group('B').reset_index(drop=True)
    group_c_matches = group_matches.get_group('C').reset_index(drop=True)
    group_d_matches = group_matches.get_group('D').reset_index(drop=True)
    group_e_matches = group_matches.get_group('E').reset_index(drop=True)
    group_f_matches = group_matches.get_group('F').reset_index(drop=True)
    group_g_matches = group_matches.get_group('G').reset_index(drop=True)
    group_h_matches = group_matches.get_group('H').reset_index(drop=True)

    return group_a_matches,group_b_matches,group_c_matches,group_d_matches,group_e_matches,group_f_matches,group_g_matches,group_h_matches
        
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

