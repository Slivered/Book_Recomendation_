import streamlit as st
st.set_page_config(layout="wide")
import sys
sys.path.append("../")
import src.Resources as src
import src.Library as lib

st.write("<h1 style='text-align: center;'>¿Con que datos estoy trabajando?</h1>", unsafe_allow_html=True)

col_big_1,col_big_2,col_big_3,col_big_4,col_big_5,col_big_6,col_big_7 = st.columns([1,1,1,1,1,1,1])
with col_big_1:
    st.metric(label="Directores",value = lib.big["Movie_directors"][0])
with col_big_2:
    st.metric(label="Actores",value = lib.big["Movie_stars"][0])
with col_big_3:
    st.metric(label="Películas",value = lib.big["Movie_titles"][0])
with col_big_4:
    st.metric(label="Géneros de películas",value = lib.big["Movie_genres"][0])
with col_big_5:
    st.metric(label="Autores",value = lib.big["Book_Authors"][0])
with col_big_6:
    st.metric(label="Libros",value = lib.big["Book_titles"][0])
with col_big_7:
    st.metric(label="Géneros de libros",value = lib.big["Book_genres"][0])

"---"
st.write("<h2 style='text-align: center;'>Comparación</h2>", unsafe_allow_html=True)
layout = {
          'margin': {'l': 40, 'r': 40, 't': 80, 'b': 40},
          'width': 800,
          'height': 400}
st.plotly_chart(src.movievsbook(),config={'displayModeBar': False, 'staticPlot': False, 'scrollZoom': False, 'editable': False},use_container_width=True,layout=layout)

st.markdown( "- Podemos apreciar que tanto las películas y los libros tienen titulos con notas maximas muy altas, 9.8 para las películas y 9.74 para los libros.")
st.markdown( "- En cuanto a las notas minimas hay una diferencia gigantesca ya que para las películas es un 1, mientras que para los libros es un 5.42.")
st.markdown( "- Y por ultimo compararemos las medias y medianas, las dos tienen resultados muy similares debido a que tengo muchos datos y los outliers se suavizan, este en concreto es el dato que más me impresiona ya que de media una película tendra una calificación de 6.5 mientras que un libro tendrá una calificación de 8.4.")
st.markdown( "La diferencia entre las notas mínimas y medias de las películas y libros se puede deber a que el mundo del cine es más complejo, incluyendo factores como el casting, los directores y los efectos especiales, lo que puede resultar en muchos factores que pueden fallar para realizar una buena película. Por otro lado, escribir un buen libro depende de menos factores ya que por lo general sólo están implicados el escritor y la editorial.")
