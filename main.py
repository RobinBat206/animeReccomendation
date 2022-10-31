# this is the start of a new program
import random
import streamlit as st
from PIL import Image
import glob
import os

st.title("Anime for all!")
listOfAnime = ["Naruto", "Dragon ball", "Bleach", "Chain Saw Man", "Digimon"]
files = os.listdir("Pictures")
#imageList = [Image.open('Pictures/1Naruto cover.jpeg'), Image.open('Pictures/2Dragon cover.jpg'), Image.open('Pictures/3bleach cover.jpeg'), Image.open('Pictures/4cm cover.jpeg'), Image.open('Pictures/5digimon cover.png')]
imageStrings = ['Pictures/1Naruto cover.jpeg', 'Pictures/2Dragon cover.jpg', 'Pictures/3bleach cover.jpeg', 'Pictures/4cm cover.jpeg', 'Pictures/5digimon cover.png']
if st.button('Click for anime'):
    #x = random.choice(listOfAnime)
    x = random.randint(0, len(listOfAnime)-1)
    y = listOfAnime[x]
    st.write("Your anime recommendation is: " + y)
    st.image(Image.open(imageStrings[x]))







