import streamlit as st
import streamlit.components.v1 as components

st.header("Data Science Students in my API6339-2024 course")

HtmlFile = open("studentsLinkedIn.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, height = 2000, width= 2000)
