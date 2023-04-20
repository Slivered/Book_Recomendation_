import pandas as pd

df = pd.read_csv('../Data/Movies_exploded.csv', index_col= 0)  
genres = list(df["Genre"].unique())