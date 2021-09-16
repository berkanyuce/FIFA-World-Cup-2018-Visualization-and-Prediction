from utilites.utilites import Pitch_class
from utilites.data_loading import goals
from utilites.dictionary import my_dictionary as dct

def show_goals_viz(home_team, away_team):

    #Create pitches for the total number of goals
    pitch = Pitch_class()
    pitch, fig, axs = pitch.create_pitch(len(goals), 1)
    
    #Goal count for show current score
    home_goal_count = 0
    away_goal_count = 0
    
    #Each iteration works for a goal
    for idx, ax in enumerate(axs[dct['pitch']].flat):

        #Goal's start positions
        x_start = goals[dct['location']][idx][0]
        y_start = goals[dct['location']][idx][1]
        
        #There are two types of goal. Goal and Own Goal.
        #Normal goals' type are 'Shot'
        if  goals[dct['type']][idx] == dct['Shot']:
            #Goal's end locations
            x_end = goals[dct['shot_end_location']][idx][0]
            y_end = goals[dct['shot_end_location']][idx][1]
            
            team_name = goals[dct['possession_team']][idx] #Get the scorer team
            
            #Show arrows by different colors. home team -> green. away team -> red
            if(team_name == home_team):
                home_goal_count += 1
                pitch.arrows(x_start, y_start, x_end, y_end, ax=ax, color='green', width=1)
                ax.text(0, -5, goals[dct['player']][idx] + "'s Goal", ha='left', va='center', fontsize=5)
                ax.text(120, -5, 'Score ' + str(home_goal_count) + " - " + str(away_goal_count), ha='right', va='center', fontsize=5)
            else:
                away_goal_count += 1
                pitch.arrows(x_start, y_start, x_end, y_end, ax=ax, color='blue', width=1)
                ax.text(0, -5, goals[dct['player']][idx] + "'s Goal", ha='left', va='center', fontsize=5)
                ax.text(120, -5, 'Score ' + str(home_goal_count) + " - " + str(away_goal_count), ha='right', va='center', fontsize=5)
       
        #Own goals' type are not 'Shot'
        else:
             #Own goals are not made by shots. So they don't have any location information.
             team_name = goals[dct['possession_team']][idx]
        
             #Show dots by different colors. home team -> green. away team -> red
             if(team_name == home_team):
                home_goal_count += 1
                pitch.scatter(x_start, y_start, ax=ax, c='green', s=6)
                ax.text(0, -5, goals[dct['player']][idx] + "'s own goal", ha='left', va='center', fontsize=5)
                ax.text(120, -5, 'Score ' + str(home_goal_count) + " - " + str(away_goal_count), ha='right', va='center', fontsize=5)

             else:
                away_goal_count += 1
                pitch.scatter(x_start, y_start, ax=ax, c='blue', s=6)
                ax.text(0, -5, goals[dct['player']][idx] + "'s Own Goal", ha='left', va='center', fontsize=5)
                ax.text(120, -5, 'Score ' + str(home_goal_count) + " - " + str(away_goal_count), ha='right', va='center', fontsize=5)
                