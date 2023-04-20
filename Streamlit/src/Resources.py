import pandas as pd
import plotly.express as px




def best_movies(genre):
    movies_exploded = pd.read_csv("../Data/Movies_exploded.csv",index_col=0)
    
    movies_genre = movies_exploded[movies_exploded["Genre"] == genre ]
    
    top_10_gen = movies_genre.sort_values(by="Rating",ascending=False).head(3)
    top_10_gen.drop("Genre",axis=1,inplace=True)
    return top_10_gen

def best_books(genre):
    books_exploded = pd.read_csv("../Data/Books_exploded.csv",index_col=0)
    
    books_genre = books_exploded[books_exploded["Genre"] == genre ]
    top_10_gen = books_genre.sort_values(by="Rating",ascending=False).head(10)
    top_10_gen.drop("Genre",axis=1,inplace=True)
    return top_10_gen

def genre_comp():
    df = pd.read_csv('../Data/genre_total.csv', index_col= 0)  
    fig = px.bar(
        df,
        x = "index",
        y = "Genre",
        color = "Type",
        barmode="group",
        color_discrete_map = {"Book": "#8aa295", "Movie": "#255957"})

    fig.update_layout(
        plot_bgcolor = "#eeebd3",
        paper_bgcolor = "#eeebd3",
        font = dict(family = "Arial", color = "#255957"))
    
    return fig