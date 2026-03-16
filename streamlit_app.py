import streamlit as st
import pickle
import pandas as pd

similarity = pickle.load(open("movie_model .pkl", "rb"))
data = pickle.load(open("movie_data .pkl", "rb"))

st.title("🎬 Movie Recommendation Chatbot")

movie_name = st.text_input("Enter Movie Name")

if st.button("Recommend"):
    try:
        movie_name = movie_name.lower()
        data["title_lower"] = data["title"].str.lower()
        index = data[data.title_lower == movie_name].index[0]
        distances = list(enumerate(similarity[index]))
        movies_list = sorted(distances, key=lambda x:x[1], reverse=True)[1:6]
        st.write("Recommended Movies:")
        for i in movies_list:
            st.write(data.iloc[i[0]].title)
    except:
        st.write("Movie not found")
