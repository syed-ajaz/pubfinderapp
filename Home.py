import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pickle

st.header("Pub Location Finder Web Application")
df = pickle.load(open('file.pkl', 'rb'))

# Basic statistics
num_pubs = len(df)
lat_range = [df["latitude"].min(), df["latitude"].max()]
long_range = [df["longitude"].min(), df["longitude"].max()]
num_authorities = len(df["Local Authority"].unique())
avg_lat = df["latitude"].mean()
avg_long = df["longitude"].mean()


st.subheader("Basic statistics")
st.write(f"Number of pubs: {num_pubs}")
st.write(f"Latitude range: {lat_range[0]} to {lat_range[1]}")
st.write(f"Longitude range: {long_range[0]} to {long_range[1]}")
st.write(f"Number of unique local authorities: {num_authorities}")
st.write(f"Average latitude: {avg_lat:.3f}")
st.write(f"Average longitude: {avg_long:.3f}")

# Display a histogram of the number of pubs by local authority
pubs_by_authority = df.groupby('Local Authority')['Pub_Name'].count().reset_index()

fig_1 = px.histogram(df, x='Local Authority',color = 'Local Authority', 
                     title='Number of Pubs in Local Authority:', width = 1000, height = 500)
st.plotly_chart(fig_1, use_container_width=True)

fig = px.scatter(df, x="latitude", y="longitude", 
                 color="Local Authority")

# Set the plot title and axis labels
fig.update_layout(title="Spatial distribution of pubs", 
                  xaxis_title="Latitude", 
                  yaxis_title="Longitude")

# Render the plot in Streamlit
st.plotly_chart(fig)