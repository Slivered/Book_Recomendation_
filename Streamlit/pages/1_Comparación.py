import streamlit as st
st.set_page_config(layout="wide")
import sys
sys.path.append("../")
import src.Resources as src
import src.Library as lib

st.write("<h1 style='text-align: center;'>Título centrado</h1>", unsafe_allow_html=True)
col_big_1,col_big_2,col_big_3,col_big_4,col_big_5,col_big_6,col_big_7 = st.columns([1,1,1,1,1,1,1])
with col_big_1:
    st.metric(label="Directores",value = lib.big["Movie_directors"][0])
with col_big_2:
    st.metric(label="Actores",value = lib.big["Movie_stars"][0])
with col_big_3:
    st.metric(label="Peliculas",value = lib.big["Movie_titles"][0])
with col_big_4:
    st.metric(label="Generos de peliculas",value = lib.big["Movie_genres"][0])
with col_big_5:
    st.metric(label="Autores",value = lib.big["Book_Authors"][0])
with col_big_6:
    st.metric(label="Libros",value = lib.big["Book_titles"][0])
with col_big_7:
    st.metric(label="Generos de libros",value = lib.big["Book_genres"][0])

st.write("<p style='text-align: center;'>asdnmbsnmBFJKDSFsdfjhkjDHDSjkdshfkjdsjkgnkjdfankkgjfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhdnkjgkjdbsgd</p>", unsafe_allow_html=True)

layout = {
          'margin': {'l': 40, 'r': 40, 't': 80, 'b': 40},
          'width': 800,
          'height': 400}
st.plotly_chart(src.movievsbook(),config={'displayModeBar': False, 'staticPlot': False, 'scrollZoom': False, 'editable': False},use_container_width=True,layout=layout)
