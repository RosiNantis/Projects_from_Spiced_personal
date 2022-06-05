 #import std libraries
from cv2 import FileStorage_INSIDE_MAP
import pandas as pd
import numpy as np
from soupsieve import select
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
# Write a title
st.title('Welcome to the Mushroom Classifier Application ')
# Write data taken from https://allisonhorst.github.io/palmerpenguins/
st.write('A **simple** *app* to explore `penguin` [data](https://allisonhorst.github.io/palmerpenguins/) :flipper: [:penguin:](https://share.streamlit.io/streamlit/emoji-shortcodes)')
# Put image https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/man/figures/lter_penguins.png
st.image('https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/man/figures/lter_penguins.png')
# Write heading for Data
st.header('Data')
# Read csv file and output a sample of 20 data points
df = pd.read_csv('penguins_extra.csv')
st.write(df)
# Add a selectbox for species
species = st.selectbox('Select your species',df.species.unique())
# Display a sample of 20 data points according to the species selected with corresponding title
df_species = df.loc[df.species == species ]
st.write(df_species.sample(20))
# Plotting seaborn
fig, ax = plt.subplots()
ax = sns.scatterplot(data = df, x= 'bill_length_mm', y= 'flipper_length_mm',hue = 'species',size='sex')
st.pyplot(fig)
# Plotting plotly

st.subheader('Interactive plotly plot')
fig = px.scatter(df, x= 'bill_length_mm', y= 'flipper_length_mm',animation_frame = 'species',range_x = [25,80],range_y = [155,250],color = 'sex')
st.plotly_chart(fig)
# Bar chart count of species per island
st.subheader('Barchart counting the number of species per island')
st.bar_chart(df.groupby('species')['island'].count())

# Maps
st.subheader('Plotting the data on a map')
st.map(df)

file = st.file_uploader('Upload csv files', type=['csv'])
if file is not None:
    data = pd.read_csv(file)
    st.write(data)

# file_img = st.file_uploader('Input image',type=['png','jpg','jpeg'])
# from PIL import Image
# if file_img is not None:
#     img = Image.open(file_img)
#     st.image(img)

  # if we want the uploader to be in the sidebar
file_img = st.sidebar.file_uploader('Input image',type=['png','jpg','jpeg'])
from PIL import Image
if file_img is not None:
    img = Image.open(file_img)
    st.image(img)
# Reference https://deckgl.readthedocs.io/en/latest/
choices = st.radio('Hope you found this interesting',['yes','no',"don't know"])
if choices =='yes':
    st.write('yes')
else:
    st.write('no')

# sidebar comment

st.markdow

st.subheader('[link for pydeck gallery](https://deckgl.readthedocs.io/en/latest/)')
st.subheader('[link for cheatsheet](https://docs.streamlit.io/library/cheatsheet)')