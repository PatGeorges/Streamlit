
import streamlit as st
#html_string = "<h3>https://rawcdn.githack.com/PatGeorges/html_files/883e5c91da9ef57128a37bba72b6de8f3385153a/particles.html</h3>"
#html_string = "<h3>/content/API6322-6339 -course promotion.html</h3>"


#path_to_html = "./https://rawcdn.githack.com/PatGeorges/html_files/883e5c91da9ef57128a37bba72b6de8f3385153a/particles.html" 

path_to_html = "API6322-6339 -course promotion2.html" 


# Read file and keep in variable
with open(path_to_html,'r') as f: 
    html_data = f.read()

## Show in webpage
st.header("Data science courses at the University of Ottawa - Patrick Georges - GSPIA/ESAPI")
st.components.v1.html(html_data, width=900, height=500)  #3600   600 ,


#st.markdown(html_string, unsafe_allow_html=True)
