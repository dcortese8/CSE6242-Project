import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle
from models import models
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title='Revenue Projections', layout="wide", page_icon="🤖")

s = """
    <style>
        div.stButton > button:first-child {{ background-color: #9D5762; color: white;  }}
    <style>
"""
st.markdown(s, unsafe_allow_html=True)

st.title('Predict Movie Theatrical Release Success')

col1, col2 = st.columns(2, gap='medium')

data = pd.read_csv('data/cleaned_movies_NEW.csv')
actor_features = pd.read_csv('data/actor_features.csv')
data = data.drop_duplicates()
genres = [x.replace('genre_','') for x in data.columns if 'genre_' in x]
keywords = [x.replace('keywords_','') for x in data.columns if 'keywords_' in x]
actors = list(set([y for x in [data['cast_1'], data['cast_2'], data['cast_3'], data['cast_4'], data['cast_5']] for y in x if str(y) != "nan"]))
input_data = {}

model_list = [" ".join(x.capitalize() for x in file.split(".")[0].split("_")) for file in os.listdir("./modeling_and_analysis/saved_models")]
st.sidebar.write('Select model to see performance fit')
mods = models(model_list)


model_name = st.sidebar.selectbox("Select Model", options=model_list)
model_file = "_".join(x.lower() for x in model_name.split(" "))
performance_plot = "".join(["./modeling_and_analysis/performance/plots/", model_file, ".png"])
performance_scores = "".join(["./modeling_and_analysis/performance/scores/", model_file, ".csv"])
# mods.load_performance(model_name)

if os.path.exists(performance_plot):
    st.sidebar.image(performance_plot, use_column_width=True) 
    if os.path.exists(performance_scores):
        scores_df = pd.read_csv(performance_scores)
        scores_df['Value'][0] = np.round(scores_df['Value'][0],4)
        scores_df['Value'][1:] = scores_df['Value'][1:].apply(lambda x: '{:.2e}'.format(x))
        st.sidebar.table(scores_df)
else:
    st.sidebar.write("No Performance Plot Found!")

with col1:
    budget = st.number_input('Budget', min_value=1, value=100000000)
    cast_size = st.number_input('Cast Size', min_value=1, value=10)
    runtime = st.number_input('Runtime (in minutes)', min_value=60, value=120)
    release_dt = st.date_input('Release Date', "today")

with col2:
    selected_genre = st.multiselect('Genre (select all that apply)', genres)
    selected_keywords = st.multiselect('Keywords (select all that apply)',keywords)
    selected_actors = st.multiselect('Enter the names of up to 5 actors to be cast', actors)

st.markdown("##")
predict_bttn = st.button('Predict Movie Success')

if predict_bttn:
    mnth = pd.to_datetime(release_dt).month_name()[:3].lower()
    wkday = pd.to_datetime(release_dt).day_name()[:3].lower()
    columns=['budget','runtime',
        'jan_release','feb_release','mar_release','apr_release','may_release',
       'jun_release','jul_release','aug_release','sep_release','oct_release',
       'nov_release','dec_release','sun_release','mon_release','tue_release',
       'wed_release','thur_release','fri_release','sat_release',
        'genre_Horror', 'genre_War',
       'genre_Adventure', 'genre_Western', 'genre_Comedy', 'genre_Mystery',
       'genre_Romance', 'genre_Science_Fiction', 'genre_Action',
       'genre_Thriller', 'genre_Crime', 'genre_TV_Movie', 'genre_Animation',
       'genre_Foreign', 'genre_Fantasy', 'genre_Drama', 'genre_Documentary',
       'genre_Family', 'genre_Music', 'genre_History','cast_size','holiday_release',
       'cast_1_vote_average','cast_2_vote_average', 'cast_3_vote_average', 'cast_4_vote_average', 'cast_5_vote_average',
       'keywords_holiday_celebrate', 'keywords_violence_war_crime',
       'keywords_superhero', 'keywords_creditstinger_3d',
       'keywords_womandirector_independentfilm',
       'keywords_future_robots_aliens',
       'keywords_edgy_alcohol_drug_sex_nudity', 'keywords_music',
       'keywords_animal_nature']
    
    input_data = {}    
    input_data['budget'] = budget
    input_data['cast_size'] = cast_size
    input_data['runtime'] = runtime
    input_data[mnth+'_release'] = 1
    input_data[wkday+'_release'] = 1
    for g in selected_genre:
        input_data['genre_'+g] = 1
    for k in selected_keywords:
        input_data['keywords_'+k] = 1
        
    for i,a in enumerate(selected_actors):
        if i < 5:
            input_data['cast_'+str(i+1)+'_vote_average'] = actor_features.loc[actor_features['cast_member_list'] == a]['vote_average'].values[0]
            
    input_data = pd.DataFrame(input_data, index=[0], columns=columns)
    input_data = input_data.fillna(0)
    
    # st.write('Test: preview input data')
    # st.table(input_data)

    mods.make_predictions(input_data)

    preds = pd.DataFrame(data=zip(mods.predictions.keys(), mods.predictions.values()), columns=['Model','Predicted Revenue'])

    preds['Predicted Revenue'] = preds['Predicted Revenue'].apply(lambda x: '${:,.2f}'.format(float(x)))

    cola1, colb1 = st.columns(2, gap='medium')
    
    with cola1:
        st.write('Average Predicted Revenue: ', '${:,.2f}'.format(mods.avg_prediction))
        st.table(preds)

    cola2, colb2 = st.columns(2, gap='medium')

    if len(selected_genre) > 0:
        for i,g in enumerate(selected_genre):
            hist_df = data[data['genre_'+g] == 1]
            perf = round(sum(hist_df.loc[hist_df['revenue_adjusted'] < float(mods.avg_prediction), 'revenue_adjusted']) * 100 / sum(hist_df['revenue_adjusted']),0)
            fig = plt.figure(figsize=(10, 4))
            sns.histplot(hist_df['revenue_adjusted'], bins=20).set(title='Revenue Spread for ' + g + ' Movies')
            if i % 2 == 0:
                with cola2:
                    st.write('Your Movie is predicted to produce more revenue than ' + str(perf) + '% of ' + g + ' Movies')
                    st.pyplot(fig)
            else:
                with colb2:
                    st.write('Your Movie is predicted to produce more revenue than ' + str(perf) + '% of ' + g + ' Movies')
                    st.pyplot(fig)