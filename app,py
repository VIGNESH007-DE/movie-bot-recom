import streamlit as st
import pickle
import pandas as pd

similarity = pickle.load(open("movie_model.pkl","rb"))
data = pickle.load(open("movie_data.pkl","rb"))

st.set_page_config(page_title="Netflix Recommender", layout="wide")

st.markdown("""
<style>
body {background-color:#141414;}
.title {color:#E50914;font-size:50px;text-align:center;font-weight:bold;}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">NETFLIX MOVIE RECOMMENDER</p>', unsafe_allow_html=True)

movie = st.text_input("Search Movie")

if st.button("Recommend"):

    movie = movie.lower()
    data["title_lower"] = data["title"].str.lower()

    index = data[data.title_lower == movie].index[0]

    distances = list(enumerate(similarity[index]))

    movies = sorted(distances, key=lambda x:x[1], reverse=True)[1:6]

    st.subheader("Recommended Movies")

    cols = st.columns(5)

    for i,m in enumerate(movies):
        with cols[i]:
            st.image("https://via.placeholder.com/200x300")
            st.write(data.iloc[m[0]].title)
