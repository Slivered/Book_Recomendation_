import pandas as pd

df = pd.read_csv('../Data/Movies_exploded.csv', index_col= 0)  
genres = list(df["Genre"].unique())
big = pd.read_csv('../Data/Bignumbers.csv', index_col= 0) 
recomendation = pd.read_csv("../Data/recomendation.csv",index_col=0)
list_rec = list(recomendation["Title"].unique())