
import pandas as pd
import streamlit as st
import folium
from folium import plugins
from streamlit_option_menu import option_menu

df_sfc = pd.read_csv('Police_Department_Incidents_-_Previous_Year__2016_.csv')
limit = 1000
df_sfc = df_sfc.iloc[0:limit, :]
df_image=pd.read_csv('books_to_scrape_utf-8-sig.csv')

st.set_page_config(
    page_title=None,
    page_icon=None,
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None,
)

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Marker/MarkerCluster Example"],
    )

# Main contents
if selected == "Marker/MarkerCluster Example":
    # Example: Crimes in San Franciso
    sanfran_map = folium.Map(location = [37.77, -122.44], zoom_start = 10)
    # get the first 10000 crimes in the df_sfc dataframe
    limit = 1000
    df_sfc = df_sfc.iloc[0:limit, :]
    # instantiate a mark cluster object for the incidents in the dataframe
    marker_cluster  = plugins.MarkerCluster().add_to(sanfran_map)
    # loop through the dataframe and add each data point to the mark cluster
    for lat, lng, label, icon in zip(df_sfc['Y'], df_sfc['X'], df_sfc['Category'], df_image['Image']):
        icon = folium.features.CustomIcon(icon,icon_size=(50, 50))
        folium.Marker([lat, lng], popup=label, icon=icon).add_to(marker_cluster)
    
    st.header("Criminality in San Francisco", divider=True)
    st.components.v1.html(folium.Figure().add_child(sanfran_map).render(), height=500)
