# this is the start of a new program
import random
import streamlit as st

st.title("Anime for all!")
listOfAnime = ["naruto", "dragon ball z", "bleach", "Chain Saw Man", "Digimon", "Pokemon"]
if st.button('Click for anime'):
    st.write("Your anime recommendation is: " + random.choice(listOfAnime))






