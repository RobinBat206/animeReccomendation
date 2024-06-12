# this is the start of a new program
import random
import streamlit as st
from PIL import Image
import glob
import os
import pandas as pd
import requests
import json


background_color = "#F0F8FF"  # Customize as needed

css = f"""
<style>
    body {{
        background-color: {background_color};
    }}
</style>
"""
st.markdown(css, unsafe_allow_html=True)


st.title("Anime for all!")
a = st.sidebar.radio("Select App:", ['Anime Recommendation', 'Game Recommendation'])
listOfAnime = ["Naruto", "Dragon ball", "Bleach", "Chain Saw Man", "Digimon"]


# upload anime from the dataframe
df = pd.read_csv("anime.csv")
df.head(10)

for dirname, _, filenames in os.walk(''):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Random generator to get recommendation from api
randomIndex = random.randint(0,12294)
randomAnime = df.iloc[randomIndex, 0]
url = f"https://api.jikan.moe/v4/anime/{randomAnime}"

# Load images into array to display

picFiles = os.listdir('Pictures')
imageList = []
for filename in picFiles:
     imageList.append('Pictures/' + filename)
     imageList.sort()



# Produce recommendation from RNG
if st.button('Click for anime'):
    randomIndex = random.randint(0, len(listOfAnime) - 1)
    randomAnime = listOfAnime[randomIndex]
    st.write("Your anime recommendation is: " + randomAnime)
    st.image(Image.open(imageList[randomIndex]))
    imageList.clear()

# randomly reccomend anime from OG list
if st.button('Random anime from database'):
    randomDfIndex = random.randint(0, len(df))
    st.write(df.loc[randomDfIndex, :].values[1])

# check to see if the dataframe has been properly loaded
if st.button('See whole database'):
     st.dataframe(df)

if st.button('Test API'):
    response = requests.get(url=url)
    json_data = json.dumps(response.json())
    data = response.json()
    # st.write(response.json())
    st.write(f"JSON Response {response.json()}")

    # st.write(json_data)
    st.write(data["data"]["title"])
    # if st.button('click for reccomendation based on genre'):
         # st.write(data['data']['episodes'])

'''# Ways to improve project

- Add more features - Be able to choose criteria for recommendations, etc.
- Find a way to make a better interface - UI, Pictures, etc
- Make a concrete plan about design 
- How do I put this out for others?


# Things I like about the project
- How it evolved over time
- Being able to use an API to get certain information

# Challenges
- Starting and stopping the project
- Getting the API to work/learning how to do that
- What different ways are there to recommend content?



'''






