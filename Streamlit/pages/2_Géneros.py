import streamlit as st
st.set_page_config(layout="wide")
import sys
sys.path.append("../")
import src.Resources as src
import src.Library as lib

st.write("<h1 style='text-align: center;'>Géneros más predominantes</h1>", unsafe_allow_html=True)

col2a,col2b = st.columns(2)
with col2b:
    st.plotly_chart(src.genre_comp_book())
with col2a:
    st.plotly_chart(src.genre_comp_movie())

st.markdown("- Películas: Drama, Acción, Comédia etc.")
st.markdown("- Libros: Historia, Fantasía, Misterio etc.")
st.markdown("- Estos resultados sugieren que la producción de contenido puede estar influenciada por las preferencias de los consumidores, y que las diferentes demandas en el mercado de libros y películas pueden tener un impacto en la diversidad y cantidad de contenido producido en cada género.")

st.write("<h2 style='text-align: center;'>Top 3 por Género</h2>", unsafe_allow_html=True)
"---"
cola,colb,colc = st.columns([1,1,2])
type = "Libro"
with cola:
    type = st.radio("¿Quieres ver el top 3 de libros o películas?",
        ("Libro","Película"))

with colb:
    genre = option = st.selectbox( "¿Qué género quieres buscar? :",
    (lib.genres))
if type == "Película":
    top3_genre = src.best_movies(genre)
elif type == "Libro":
    top3_genre = src.best_books(genre)
image1 = (list(top3_genre["Image"]))[0]
image2 = (list(top3_genre["Image"]))[1]
image3 = (list(top3_genre["Image"]))[2]
title1 = (list(top3_genre["Title"]))[0]
title2 = (list(top3_genre["Title"]))[1]
title3 = (list(top3_genre["Title"]))[2]
description1 = (list(top3_genre["Description"]))[0]
description2 = (list(top3_genre["Description"]))[1]
description3 = (list(top3_genre["Description"]))[2]
rating1 = (list(top3_genre["Rating"]))[0]
rating2 = (list(top3_genre["Rating"]))[1]
rating3 = (list(top3_genre["Rating"]))[2]
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

    
    