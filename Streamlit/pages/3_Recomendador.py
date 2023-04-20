import streamlit as st
st.set_page_config(layout="wide")
import sys
sys.path.append("../")
import src.Resources as src
import src.Library as lib


recomended = option = st.selectbox( "Which genre would you like to see? :",
    (lib.list_rec))
type = st.radio(
    "¿Quieres peliculas o libros?",
    ("Pelicula","Libro"))
if type == "Pelicula":
    type = "Movie"
else:
    type = "Book"

recomendation = src.top(recomended,type)

image1 = (list(recomendation["Image"]))[0]
image2 = (list(recomendation["Image"]))[1]
image3 = (list(recomendation["Image"]))[2]
title1 = (list(recomendation["Title"]))[0]
title2 = (list(recomendation["Title"]))[1]
title3 = (list(recomendation["Title"]))[2]
description1 = (list(recomendation["Description"]))[0]
description2 = (list(recomendation["Description"]))[1]
description3 = (list(recomendation["Description"]))[2]
rating1 = (list(recomendation["Rating"]))[0]
rating2 = (list(recomendation["Rating"]))[1]
rating3 = (list(recomendation["Rating"]))[2]
if len(description1)> 600: 
    description1 = description1[:600] +"..."
if len(description2)> 600 : 
    description2 = description2[:600] +"..."
if len(description3)> 600 : 
    description3 = description3[:600] +"..."

col_p_1, col_p_2, col_p_3 = st.columns([1,3,1])

with col_p_1:
    st.image(image1,width = 150)

with col_p_2:
    st.write(f"<h5 style='text-align: center;'>{title1}</h5>", unsafe_allow_html=True)
    st.write(f"<p style='text-align: center;'>{description1}</p>", unsafe_allow_html=True)

with col_p_3:
    st.write(f"<h1 style='text-align: center;'>{rating1}</h1>", unsafe_allow_html=True)

col_s_1, col_s_2, col_s_3 = st.columns([1,3,1])

with col_s_1:
    st.image(image2,width = 150)

with col_s_2:
    st.write(f"<h5 style='text-align: center;'>{title2}</h5>", unsafe_allow_html=True)
    st.write(f"<p style='text-align: center;'>{description2}</p>", unsafe_allow_html=True)

with col_s_3:
    st.write(f"<h1 style='text-align: center;'>{rating2}</h1>", unsafe_allow_html=True)

col_t_1, col_t_2, col_t_3 = st.columns([1,3,1])

with col_t_1:
    st.image(image3,width = 150)

with col_t_2:
    st.write(f"<h5 style='text-align: center;'>{title3}</h5>", unsafe_allow_html=True)
    st.write(f"<p style='text-align: center;'>{description3}</p>", unsafe_allow_html=True)

with col_t_3:
    st.write(f"<h1 style='text-align: center;'>{rating3}</h1>", unsafe_allow_html=True)