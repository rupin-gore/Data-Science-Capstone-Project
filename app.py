import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Set page config
st.set_page_config(
    page_title="SpaceX Falcon 9 Launch Analysis",
    page_icon="🚀",
    layout="wide"
)

# Title and description
st.title("SpaceX Falcon 9 Launch Analysis Dashboard")
st.markdown("""
This dashboard analyzes SpaceX Falcon 9 launch data to predict first stage landing success.
Explore the data and visualizations below to understand the factors that influence successful landings.
""")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('dataset_part_2.csv')
    return df

# Load the data
df = load_data()

# Sidebar for filters
st.sidebar.header("Filters")
launch_sites = df['LaunchSite'].unique()
selected_site = st.sidebar.selectbox('Select Launch Site', launch_sites)

# Filter data based on selection
filtered_df = df[df['LaunchSite'] == selected_site]

# Main content
st.header("Launch Site Analysis")

# Success rate by launch site
st.subheader("Success Rate by Launch Site")
success_rate = df.groupby('LaunchSite')['Class'].mean().reset_index()
fig = px.bar(success_rate, x='LaunchSite', y='Class', 
             title='Success Rate by Launch Site',
             labels={'Class': 'Success Rate', 'LaunchSite': 'Launch Site'})
st.plotly_chart(fig, use_container_width=True)

# Payload mass vs Success
st.subheader("Payload Mass vs Success")
fig = px.scatter(df, x='PayloadMass', y='Class', 
                 color='LaunchSite',
                 title='Payload Mass vs Success Rate',
                 labels={'PayloadMass': 'Payload Mass (kg)', 'Class': 'Success'})
st.plotly_chart(fig, use_container_width=True)

# Orbit type analysis
st.subheader("Success Rate by Orbit Type")
orbit_success = df.groupby('Orbit')['Class'].mean().reset_index()
fig = px.bar(orbit_success, x='Orbit', y='Class',
             title='Success Rate by Orbit Type',
             labels={'Class': 'Success Rate', 'Orbit': 'Orbit Type'})
st.plotly_chart(fig, use_container_width=True)

# Data table
st.subheader("Launch Data")
st.dataframe(filtered_df, use_container_width=True)

# Add footer
st.markdown("---")
st.markdown("Data Source: SpaceX API and Web Scraping") 
