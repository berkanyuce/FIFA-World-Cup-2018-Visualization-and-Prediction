
my_dictionary = {
    #Variables Dictionary. These variables are used by dataframes, creating variables, etc.
    #Variables in this dictionary are may will changange in the future. So, If it happens, I only change these dictinary not all project.
    #These variables are used on only column names and comparisons. Functions parameters, colors, positions are not included in dictionary.
    
    'Final' : 'Final', 
    'Third Place' : 'Third Place',
    'Semi Finals' : 'Semi Finals',
    'Select Match' : 'Select Match',
    'home_team' : 'home_team',
    'away_team' : 'away_team',
    'Full_Match_Info' : 'Full_Match_Info',
    'Select Analyze Type' : 'Select Analyze Type',
    'Match Analyze' : 'Match Analyze',
    'Team Analyze' : 'Team Analyze',
    'Player Analyze' : 'Player Analyze',
    'Select Event Type' : 'Select Event Type',
    'Quarter Finals' : 'Quarter Finals',
    'Round of 16' : 'Round of 16',
    'Group Stage' : 'Group Stage',
    'Select Group' : 'Select Group',
    'Group A' : 'Group A',
    'Group B' : 'Group B',
    'Group C' : 'Group C',
    'Group D' : 'Group D',
    'Group E' : 'Group E',
    'Group F' : 'Group F',
    'Group G' : 'Group G',
    'Group H' : 'Group H',
    'A' : 'A',
    'B' : 'B',
    'C' : 'C',
    'D' : 'D',
    'E' : 'E',
    'F' : 'F',
    'G' : 'G',
    'H' : 'H',
    'Select Team' : 'Select Team',
    '.png' : '.png',
    'minute' : 'minute',
    'Score' : 'Score',
    'team' : 'team',
    'Compare Type' : 'Compare Type',
    'player' : 'player',
    'Line Up' : 'Line Up',
    'Pass Networks' : 'Pass Networks',
    'Shots Map by xG' : 'Shots Map by xG',
    'Lineups' : 'Lineups',
    'Goals' : 'Goals',
    'Heat Maps' : 'Heat Maps',
    'xG Expected Goals' : 'xG Expected Goals',
    'Shots Map by Using xG' : 'Shots Map by Using xG',
    'TeamLogos' : 'TeamLogos',
    'competition_stage' : 'competition_stage',
    'match_id' : 'match_id',
    'nan' : 'nan',
    'player_name' : 'player_name',
    'Pass' : 'Pass',
    'Shot' : 'Shot',
    'id' : 'id',
    'Goal' : 'Goal',
    'type' : 'type',
    'Own Goal Against' : 'Own Goal Against',
    'pass_recipient_id' : 'pass_recipient_id',
    'possession_team' : 'possession_team',
    'shot_outcome' : 'shot_outcome',
    'location' : 'location',
    'shot_statsbomb_xg' : 'shot_statsbomb_xg',
    '(OG)' : '(OG)',
    'pass_outcome' : 'pass_outcome',
    'Success' : 'Success',
    'pass_end_location' : 'pass_end_location',
    'pitch' : 'pitch',
    'shot_end_location' : 'shot_end_location',
    'tactics' : 'tactics',
    'lineup' : 'lineup',
    'position' : 'position',
    'jersey_number' : 'jersey_number',
    'name' : 'name',
    'x' : 'x',
    'y' : 'y',
    'position_id' : 'position_id',
    'position_x' : 'position_x',
    'position_y' : 'position_y',
    'Substitution' : 'Substitution',
    'count' : 'count',
    'mean' : 'mean',
    '_end' : '_end',
    'Team' : 'Team',
    'Group Name' : 'Group Name',
    'home_score' : 'home_score',
    'away_score' : 'away_score',
    'player_id' : 'player_id',
    'pass_count' : 'pass_count',
    'pass_recipient' : 'pass_recipient',
    
    #Positions Dictionary
    1: {
        'name': 'Goalkeeper',        
        'x': 0,
        'y': 40
    },
    2: {
        'name': 'Right Back',        
        'x': 25,
        'y': 13.3
    },
    3: {
        'name': 'Righ Center Back',        
        'x': 20,
        'y': 26.6
    },
    4: {
        'name': 'Center Back',        
        'x': 20,
        'y': 40
    },
    5: {
        'name': 'Left Center Back',        
        'x': 20,
        'y': 53.4
    },
    6: {
        'name': 'Left Back',        
        'x': 25,
        'y': 66.7
    },
    7: {
        'name': 'Right Wing Back',        
        'x': 45,
        'y': 13.3
    },
    8: {
        'name': 'Left Wing Back',        
        'x': 45,
        'y': 66.7
    },
    9: {
        'name': 'Right Defensive Midfield',        
        'x': 40,
        'y': 26.6
    },
    10: {
        'name': 'Center Defensive Midfield',        
        'x': 40,
        'y': 40
    },
    11: {
        'name': 'Left Defensive Midfield',        
        'x': 40,
        'y': 53.4
    },
    12: {
        'name': 'Right Midfield',        
        'x': 65,
        'y': 13.3
    },
    13: {
        'name': 'Right Center Midfield',        
        'x': 60,
        'y': 26.6
    },
    14: {
        'name': 'Center Midfield',        
        'x': 60,
        'y': 40
    },
    15: {
        'name': 'Left Center Midfield',        
        'x': 60,
        'y': 53.4
    },
    16: {
        'name': 'Left Midfield',        
        'x': 65,
        'y': 66.7
    },
    17: {
        'name': 'Right Wing',        
        'x': 85,
        'y': 13.3
    },
    18: {
        'name': 'Right Attacking Midfield',        
        'x': 80,
        'y': 26.6
    },
    19: {
        'name': 'Center Attacking Midfield',        
        'x': 80,
        'y': 40
    },
    20: {
        'name': 'Left Attacking Midfield',        
        'x': 80,
        'y': 53.4
    },
    21: {
        'name': 'Left Wing',        
        'x': 85,
        'y': 66.7
    },
    22: {
        'name': 'Right Center Forward',        
        'x': 100,
        'y': 20
    },
    23: {
        'name': 'Center Forward',        
        'x': 100,
        'y': 40
    },
    24: {
        'name': 'Left Center Forward',        
        'x': 100,
        'y': 60
    }
}

