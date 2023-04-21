import streamlit as st
st.set_page_config(layout="wide")
import sys
sys.path.append("../")
import src.Resources as src
st.write("<h1 style='text-align: center;'>El mundo del cine contra el mundo literario</h1>", unsafe_allow_html=True)
st.image("../images/Book2.jpg",use_column_width=True)
"---"
st.write("<p style='text-align: left;'>La literatura y el cine son dos formas de arte populares que tienen como objetivo contar historias y transmitir emociones mediante diversas técnicas narrativas y visuales.</p>", unsafe_allow_html=True)
st.write("<p style='text-align: left;'>Aunque ambos medios comparten esta similitud, también presentan diferencias significativas en cómo se cuentan sus historias. Personalmente, me interesa explorar esta comparación y explorar cuál de los dos medios cumple mejor este objetivo.</p>", unsafe_allow_html=True)
"---"
st.write("<h2 style='text-align: center;'>Metodología</h2>", unsafe_allow_html=True)
st.markdown("- Recolección de datos: Como parte de este proyecto, realicé un scrapeo de datos tanto de Goodreads como de imdb para obtener información relevante sobre películas y libros.")
st.markdown("- Tratamiento y limpieza de datos: Una vez que obtuve los datos, realicé una limpieza y homogenización para garantizar que los datos fueran coherentes y utilizables en mi análisis.")
st.markdown("- Análisis: Utilicé herramientas de visualización de datos para crear gráficas y un filtro interactivo para representar y explorar los datos en profundidad.")
st.markdown("- Modelaje: Y para finalizar el proyecto preparé un modelo recomendador que utiliza técnicas de machine learning para sugerir contenido similar a una película o libro de entrada.")

