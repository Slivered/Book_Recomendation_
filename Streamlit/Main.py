import streamlit as st
st.set_page_config(layout="wide")
import sys
sys.path.append("../")
import src.Resources as src
st.write("<h1 style='text-align: center;'>Título centrado</h1>", unsafe_allow_html=True)
st.image("../images/cine2.jpg",use_column_width=True)
