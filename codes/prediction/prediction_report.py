import streamlit as st
import streamlit.components.v1 as components
from utilites.data_loading import DATADIR
import urllib

def prediction_report():
    
    st.subheader('Abstract')
    st.text('''
            The purpose of this model is to predict match results of FIFA World Cup 2018 using the match results 
            between 2004-2018 and the teams' FIFA rank. Worked on the 2018 World Cup. Because there is an opportunity 
            to test the results. 
            
            Features are planned as teams' market values, world rank, and a point given for the team lineup. But, 
            the market values of teams can not be found in the old years. Unfortunately, market values are not included 
            in the model. Instead, features were selected as team powers(Attack, Middle, Defense, and Overall) on 
            associated FIFA games and FIFA ranks.
            
            The model's goal is to find the winner. So, the model should give answers like -1 or 1. This means there is 
            a classification problem. 3 different models are tested for this model. These are Logistic Regression (LR), 
            Support Vector Machine (SVM), and Random Forest Classifier (RFC). LR and SVM are working at the same accuracy 
            but SVM works more consistently. So, SVM was used in the model.
            
            2018 World Cup was a surprising tournament. Germany's elimination on group stage, Spain's loss against Russia 
            were unexpected results. Except these unexpected results the model works accetable. Let's analyze!
            
            ''')
    
    st.subheader('Visualization of Data')
    height = 450
    
    st.text('''
            Before creating the model, let's look into the data. If we look at the power distribution of the teams we 
            have knowledge of by years, the power of the teams participating in the World Cup is above the average 
            power of the other teams. And, the small power differences between these teams are clearly visible. Also,
            According to this statistics, Spain is the most powerful team since 2007.
            ''')
        
    url = DATADIR + "codes/prediction/team_powers_scatter.html"
    r = urllib.request.urlopen(url).read()
    components.html(r, height=height)

    url = DATADIR + "codes/prediction/team_powers_bar.html"
    r = urllib.request.urlopen(url).read()
    components.html(r, height=height)
    
    url = DATADIR + "codes/prediction/team_powers_3d.html"
    r = urllib.request.urlopen(url).read()
    components.html(r, height=height)
    
    st.text('''
            Looking at the teams' powers and goal differences, the teams that have more power have more goal differences
            not surprisingly. Also, goal differences are generally between -1 and 1. This means national matches are more 
            competitive. But, it is caused predicting the results more difficult.
            ''')
   
    url = DATADIR + "codes/prediction/team_powers_scores.html"
    r = urllib.request.urlopen(url).read()
    components.html(r, height=height)
    
    st.subheader('Comparing Models')

    st.text('''
            The graph at the below shows differences between three machine learning models' performance. The Support
            Vector Machine was chosen as the model because it produces both a high accuracy and a stable result.
            
            The figure under this graph shows how many tries need to get stable result from model. After than apporixmatly 
            6500 tries the model is giving stable results. So, all matches simulated 6500 times.
            ''')
    

    url = DATADIR + "codes/prediction/compare_models_viz.html"
    r = urllib.request.urlopen(url).read()
    components.html(r, height=height)
    
    url = DATADIR + "codes/prediction/number_of_simulastions_viz.html"
    r = urllib.request.urlopen(url).read()
    components.html(r, height=height)
    
    st.subheader('Predicting The Tournament')
    st.text('''
            The knockout stage was predicted by using Support Vector Machine as shown at below.
            ''')
   
    st.image(DATADIR + 'codes/prediction/world_cup_simulation_tree.jpeg')
    
    st.text('''
            The model failed this try. Because there are some suprised results like Spain - Russia. If one match is
            predicted wrong, remaining matches can also be predicted incorrectly. That's why, we should predict match by match.
            When we do that, we get better results. The model correctly predicted 11 out of 16 matches. When we look
            If we look at the odds of the matches, it is possible to earn 2173 dollars against 1600 dollars at the end of the 
            tournament when 100 dollars are bet on each match. This means 35 percent profit.
            ''')
    
    st.image(DATADIR + 'codes/prediction/match-by-match.jpeg')
    
    st.subheader('Conclusion')
    st.text('''
            2018 World Cup was a surprising tournament. The model failed these surprised matches. But made good 
            prediction on two equal teams' matches like Denmark-Croatia. It can be clearly seen that the FIFA 
            ranking of the teams is effective  on the match results. Also, Spain's rank and power affected to 
            model's prediction.
            
            But France won this tournament in reality. If only reference to match results, predict the France's winning 
            so difficult. But when compare market values, France was the most valuable team at the tournament. 
            Unfortunately, there are no data about old years' team market values. 
            
            At the other hands, If we can predict match by match, we can get good results and we have been shown that 
            profit can be made using machine learning.
            ''')   
