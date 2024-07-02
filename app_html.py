import streamlit as st
import streamlit.components.v1 as components

st.header("My students in API6339 'Data Science Projects' Summer 2024, uOttawa")

HtmlFile = open("API6339_2024_network_hyperlinks.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, height = 800, width=800)  #, , width= 2000
