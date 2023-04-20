import streamlit as st

import sys
sys.path.append("../")
import src.Resources as src
import src.Library as lib


st.title("Genre")

#st.header("asdsadasd")

st.write("Holadskfjskdnfkldsnfklsndklfjdsklfklsdjflksjgkdsjklgdnkssssssssssssssssssdddd")
#st.markdown("- Hola")
#st.write("asjdhasdnbasnfbkjsfnaf")
st.plotly_chart(src.genre_comp())
col1a,col2a,col3a = st.columns([1,1,5])
type = "book"
with col2a:

    if st.button("Movies"):
        type ="movie"
with col1a:
    if st.button("Books"):
        type="book"

genre = option = st.selectbox( 'How would you like to be contacted?',
    (lib.genres))
if type == "movie":
    top3_genre = src.best_movies(genre)
elif type == "book":
    top3_genre = src.best_books(genre)
image1 = (list(top3_genre["Image"]))[0]
image2 = (list(top3_genre["Image"]))[1]
image3 = (list(top3_genre["Image"]))[2]
title1 = (list(top3_genre["Title"]))[0]
title2 = (list(top3_genre["Title"]))[1]
title3 = (list(top3_genre["Title"]))[2]
desc1 = (list(top3_genre["Description"]))[0]
desc2 = (list(top3_genre["Description"]))[1]
desc3 = (list(top3_genre["Description"]))[2]
col1, col2, col3 = st.columns(3)


with col1:
    st.subheader(title1)
    st.image(image1)
    st.write(desc1)

with col2:
    st.subheader(title2)
    st.image(image2)
    st.write(desc2)
with col3:
    st.subheader(title3)
    st.image(image3)
    st.write(desc3)