import streamlit as st 
import pickle 
import pandas as pd
import requests

def fetch_poster(movie_id):
    response =requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2ec00fcd2e0bf9c04ae8f796a9374249&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    answer = sorted(list(enumerate(distances)) , reverse = True , key = lambda x : x[1])[1:6]

    recommended = []
    posters = []
    for i in answer :
        movie_id = movies.iloc[i[0]].movie_id
        recommended.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))
    return recommended , posters
movies_dict = pickle.load(open('movies_dict.pkl' , 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl' , 'rb'))
st.title('Movie Recommender System')

selected_movie = st.selectbox('Choose the movie you like ' , movies['title'].values)

if st.button('Recommend'):
    names , pictures = recommend(selected_movie)
    col1 , col2 , col3 , col4 , col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(pictures[0])

    with col2:
        st.text(names[1])
        st.image(pictures[1])

    with col3:
        st.text(names[2])
        st.image(pictures[2])

    with col4:
        st.text(names[3])
        st.image(pictures[3])

    with col5:
        st.text(names[4])
        st.image(pictures[4])