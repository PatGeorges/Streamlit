
import pandas as pd
import streamlit as st
import folium
from folium import plugins
from streamlit_option_menu import option_menu

datafile1 = "vancouver.csv"
datafile2 = "local_area_boundary_vancouver.geojson"

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
        options=["Marker/MarkerCluster Example", "GeoJson Example"],
    )

# Main contents
if selected == "Marker/MarkerCluster Example":
    # Example: EV Charging Stations in the Vancouver" (CSV file)

    df_vancouver = pd.read_csv('vancouver.csv', delimiter=',')
    latitude = 49.28
    longitude = -123.13
    # create map and display it
    vancouver_map = folium.Map(location=[latitude, longitude], zoom_start=10)

    # instantiate a mark cluster object for the ev_charging stations in the dataframe
    marker_cluster = plugins.MarkerCluster().add_to(vancouver_map)

    # loop through the dataframe and add each data point to the mark cluster
    for lat, lng, street, in zip(df_vancouver['Latitude'], df_vancouver['Longitude'], df_vancouver['Address']):
        folium.Marker(
           location=[lat, lng],
           icon=None,
           popup=street,
           ).add_to(marker_cluster)

    st.header("EV Charging Stations in the Vancouver", divider=True)
    st.components.v1.html(folium.Figure().add_child(vancouver_map).render(), height=500)

    #Show the data table
    st.write("Data Table")
    dataframe = pd.read_csv('vancouver.csv') #, delimiter=","
    st.write(dataframe)

    # Show the data source
    link = "[CITY OF VANCOUVER OPEN DATA PORTAL - Electric vehicle charging stations](https://opendata.vancouver.ca/explore/dataset/electric-vehicle-charging-stations/export/)"
    st.markdown("Data Source: " + link, unsafe_allow_html=True)

elif selected == "GeoJson Example":
    # Example: Local Area Boundary in the Vancouver (GeoJson file)

    map2 = folium.Map(location=[49.255, -123.13], zoom_start=12)

    popup = folium.GeoJsonPopup(
        fields=["geo_local_area"],  #choose among "geo_local_area", "geo_point_2d",  "lot_operator"
        aliases=["geo_localisation:"],
    )

    folium.GeoJson(
        datafile2,
        popup=popup,
    ).add_to(map2)

    st.header("Local Area Boundary in the Vancouver (GeoJSON)", divider=True)
    st.components.v1.html(folium.Figure().add_child(map2).render(), height=500)

    # Show the data source
    link = "[CITY OF VANCOUVER OPEN DATA PORTAL - Local area boundary](https://opendata.vancouver.ca/explore/dataset/local-area-boundary/export/)"
    st.markdown("Data Source: " + link, unsafe_allow_html=True)
