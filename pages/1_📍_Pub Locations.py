import streamlit as st
from streamlit_folium import st_folium
import pickle, folium

# Load data
df = pickle.load(open('file.pkl', 'rb'))

#Streamlit app
st.title("Pub Locations")
st.write("This map shows the locations of all the pubs in the UK.")

def filter_pubs(filter_type, filter_value):
    if filter_type == 'Postal Code':
        filtered_pubs = df[df['Postal Code'] == filter_value]
    elif filter_type == 'Local Authority':
        filtered_pubs = df[df['Local Authority'] == filter_value]
    else:
        filtered_pubs = df
    
    return filtered_pubs

# Ask the user to select the filter type and value
filter_type = st.radio("Search by",["Postal Code", "Local Authority"])
if filter_type == 'Postal Code':
    filter_value = st.selectbox('Select Postal Code:', options=df['Postal Code'].unique())
elif filter_type == 'Local Authority':
    filter_value = st.selectbox('Select Local Authority:', options=df['Local Authority'].unique())
else:
    filter_value = None

# Filter the pubs based on the selected filter type and value
filtered_pubs = filter_pubs(filter_type, filter_value)

# Display the number of pubs in the selected area
st.write(f"Number of pubs in {filter_value}: {len(filtered_pubs)}")

# Display the filtered pubs on a map
m = folium.Map(location=[filtered_pubs['latitude'].mean(), filtered_pubs['longitude'].mean()], zoom_start=13)

for index, row in filtered_pubs.iterrows():
    pub_name = row['Pub_Name']
    pub_lat = row['latitude']
    pub_lon = row['longitude']
    
    folium.Marker([pub_lat, pub_lon], popup=pub_name).add_to(m)
map = st_folium(m, width = 725)