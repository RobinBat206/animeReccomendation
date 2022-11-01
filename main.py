# this is the start of a new program
import random
import streamlit as st
from PIL import Image
import glob
import os

st.title("Anime for all!")
listOfAnime = ["Naruto", "Dragon ball", "Bleach", "Chain Saw Man", "Digimon"]
files = os.listdir('Pictures')
imageList = []
for filename in files:
    imageList.append('Pictures/' + filename)
    imageList.sort()

if st.button('Click for anime'):
    randomIndex = random.randint(0, len(listOfAnime)-1)
    randomAnime = listOfAnime[randomIndex]
    st.write("Your anime recommendation is: " + randomAnime)
    st.image(Image.open(imageList[randomIndex+1])) #Have to use +1 because file .DS store is always in directory
    imageList.clear()







