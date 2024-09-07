import pickle
import streamlit as st
import requests


movies_list = pickle.load(open('movies.pkl','rb'))
similarity_list = pickle.load(open('similarity.pkl','rb'))

def get_movie_poster(movie_name):
    prefix_link = "https://www.omdbapi.com/?apikey=e916e59d&t="
    res = requests.get(prefix_link + movie_name)
    poster_link = res.json()['Poster']
    re = requests.get(poster_link)
    return re.content

def recommend(movie):
    index = movies_list[movies_list['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity_list[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies_list.iloc[i[0]].movie_id
        recommended_movie_names.append(movies_list.iloc[i[0]].title)
        recommended_movie_posters.append(get_movie_poster(movies_list.iloc[i[0]].title))
    return recommended_movie_names,recommended_movie_posters


lst = movies_list['title'].values
st.title("Movie Recommendation System using Machine Learning")
Selected_movie_name = st.selectbox(
    'Select any Movie: ',(lst)
)
if st.button('Recommend Movies related to selected Movies'):

    recommended_movie_names, recommended_movie_posters = recommend(Selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
