import streamlit as st
from streamlit_folium import st_folium
import numpy as np
import pickle, folium
from math import sqrt

# Load the dataset
df = pickle.load(open('file.pkl', 'rb'))

# Define the Streamlit app layout
st.title("Find the nearest pub")
col1, col2 = st.columns(2)
with col1 :
    latitude = st.number_input('Latitude')
    col1 = st.write('The Latitude is ', latitude)
with col2:
    longitude = st.number_input('Longitude')
    col2 = st.write('The Longitude is ', longitude)

# Define a function to calculate the Euclidean distance between two points
def euclidean_distance(lat1, lon1, lat2, lon2):
    return np.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

# Calculate the distances between the user and each pub
df['distance'] = df.apply(lambda row: euclidean_distance(row['latitude'], row['longitude'], latitude, longitude), axis=1)

# Find the 5 nearest pubs
nearest_pubs = df.sort_values('distance').head(5)

# Display the nearest pubs on a map
m = folium.Map(location=[latitude, longitude], zoom_start=0)

for index, row in nearest_pubs.iterrows():
    pub_name = row['Pub_Name']
    pub_lat = row['latitude']
    pub_lon = row['longitude']
    pub_distance = row['distance']
    
    folium.Marker([pub_lat, pub_lon], popup=f"{pub_name}, {pub_distance:.2f} km").add_to(m)

st.write(nearest_pubs)
map = st_folium(m, width = 1000)