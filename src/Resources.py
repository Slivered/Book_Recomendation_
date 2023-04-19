from selenium import webdriver
import numpy as np
import pandas as pd
from time import sleep
import pickle
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import warnings
warnings.filterwarnings('ignore')
driver = webdriver.Chrome(ChromeDriverManager().install())
import src.Library as lib
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
from itertools import combinations

#Resources to scrap goodreads.

"""
This function takes a list as input and appends book information to it, including author, image URL,
description, book rating, number of votes, book title, and genres. It then navigates back to the previous
page on Goodreads.com.

Args:
- list2 (list): The list to which the book information is appended.

Returns:
- list2 (list): The updated list with appended book information.
"""
def targets(list2):
            
            inner = []
            try:
                #Author

                inner.append(driver.find_element("css selector","#__next > div > main > div.BookPage__gridContainer > div.BookPage__rightColumn > div.BookPage__mainContent > div.BookPageMetadataSection > div.BookPageMetadataSection__contributor > h3 > div > span:nth-child(1) > a > span.ContributorLink__name").text)

                #Image Url
                inner.append(driver.find_element("css selector","#__next > div > main > div.BookPage__gridContainer > div.BookPage__leftColumn > div > div.BookPage__bookCover > div > div > div > div > div > div > img").get_attribute("src"))

                #Description

                inner.append(driver.find_element("css selector","#__next > div > main > div.BookPage__gridContainer > div.BookPage__rightColumn > div.BookPage__mainContent > div.BookPageMetadataSection > div.BookPageMetadataSection__description > div > div.TruncatedContent__text.TruncatedContent__text--large > div > div").text)
                
                #Book rating

                inner.append(driver.find_element("css selector","#__next > div > main > div.BookPage__gridContainer > div.BookPage__rightColumn > div.BookPage__mainContent > div.BookPageMetadataSection > div.BookPageMetadataSection__ratingStats > a > div:nth-child(1) > div").text)

                #Number of votes

                inner.append(driver.find_element("css selector","#__next > div > main > div.BookPage__gridContainer > div.BookPage__rightColumn > div.BookPage__mainContent > div.BookPageMetadataSection > div.BookPageMetadataSection__ratingStats > a > div:nth-child(2) > div > span:nth-child(1)").text)
        
                #Book title

                inner.append(driver.find_element("css selector","#__next > div > main > div.BookPage__gridContainer > div.BookPage__rightColumn > div.BookPage__mainContent > div.BookPageTitleSection > div.BookPageTitleSection__title > h1").text)
                
                genres = []
                genres.append(driver.find_element("css selector","#__next > div > main > div.BookPage__gridContainer > div.BookPage__rightColumn > div.BookPage__mainContent > div.BookPageMetadataSection > div.BookPageMetadataSection__genres > ul > span:nth-child(1) > span:nth-child(2) > a > span").text)
                genres.append(driver.find_element("css selector","#__next > div > main > div.BookPage__gridContainer > div.BookPage__rightColumn > div.BookPage__mainContent > div.BookPageMetadataSection > div.BookPageMetadataSection__genres > ul > span:nth-child(1) > span:nth-child(3) > a > span").text)
                genres.append(driver.find_element("css selector","#__next > div > main > div.BookPage__gridContainer > div.BookPage__rightColumn > div.BookPage__mainContent > div.BookPageMetadataSection > div.BookPageMetadataSection__genres > ul > span:nth-child(1) > span:nth-child(4) > a > span").text)
                genres.append(driver.find_element("css selector","#__next > div > main > div.BookPage__gridContainer > div.BookPage__rightColumn > div.BookPage__mainContent > div.BookPageMetadataSection > div.BookPageMetadataSection__genres > ul > span:nth-child(1) > span:nth-child(5) > a > span").text)
                inner.append(genres)
                list2.append(inner)
                driver.back()
                return list2
            except:
                driver.back()

#Main function that scraps the  book genre of your choice from goodreads
def search(genre,Email,Password):
    list=[]
    driver.get("https://www.goodreads.com/ap/signin?openid.return_to=https%3A%2F%2Fwww.goodreads.com%2Fap-handler%2Fregister&prevRID=0VAZ87TY1RWA25KR8J6B&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_goodreads_web_na&openid.mode=checkid_setup&siteState=46758e455d4a0ed27384a4c1de5a69e0&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=amzn_goodreads_web_na&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
    driver.find_element("css selector","#ap_email").click()
    driver.find_element("css selector","#ap_email").send_keys(Email)
    driver.find_element("css selector","#ap_password").click()
    driver.find_element("css selector","#ap_password").send_keys(Password)
    driver.find_element("css selector","#signInSubmit").click()
    driver.implicitly_wait(30)

    for gen in genre:
        try:
            driver.find_element("css selector","body > div.siteHeader > div > header > div.siteHeader__topLine.gr-box.gr-box--withShadow > div > div.searchBox.searchBox--navbar > form > input.searchBox__input.searchBox__input--navbar").click()
            driver.find_element("css selector","body > div.siteHeader > div > header > div.siteHeader__topLine.gr-box.gr-box--withShadow > div > div.searchBox.searchBox--navbar > form > input.searchBox__input.searchBox__input--navbar").send_keys(gen,Keys.ENTER)
            driver.find_element("css selector","body > div.content > div.mainContentContainer > div.mainContent > div.mainContentFloat > div.leftContainer > div.greyText > a:nth-child(2)").click()
            try:
                driver.find_element("css selector","body > div.content > div.mainContentContainer > div.mainContent > div.mainContentFloat > div.leftContainer > div:nth-child(8) > div.bigBoxBody > div > div.moreLink > a").click()
            except:
                driver.find_element("css selector","body > div.content > div.mainContentContainer > div.mainContent > div.mainContentFloat > div.leftContainer > div:nth-child(7) > div.bigBoxBody > div > div.moreLink > a").click()
        except:
            driver.find_element("css selector","body > div.content > div.siteHeader > div > header > div.siteHeader__topLine.gr-box.gr-box--withShadow > div > div.searchBox.searchBox--navbar > form > input.searchBox__input.searchBox__input--navbar").click()
            driver.find_element("css selector","body > div.content > div.siteHeader > div > header > div.siteHeader__topLine.gr-box.gr-box--withShadow > div > div.searchBox.searchBox--navbar > form > input.searchBox__input.searchBox__input--navbar").send_keys(gen,Keys.ENTER)
            driver.find_element("css selector","body > div.content > div.mainContentContainer > div.mainContent > div.mainContentFloat > div.leftContainer > div.greyText > a:nth-child(2)").click()
            try:
                driver.find_element("css selector","body > div.content > div.mainContentContainer > div.mainContent > div.mainContentFloat > div.leftContainer > div:nth-child(8) > div.bigBoxBody > div > div.moreLink > a").click()
            except:
                driver.find_element("css selector","body > div.content > div.mainContentContainer > div.mainContent > div.mainContentFloat > div.leftContainer > div:nth-child(7) > div.bigBoxBody > div > div.moreLink > a").click()

        for page in range (24):
            for i in range(4,101,2):
                try: 
                    iterator = str(i)
                    link = "body > div.content > div.mainContentContainer > div.mainContent > div.mainContentFloat > div.leftContainer > div:nth-child("+ iterator +") > div.left > a.bookTitle"
                    driver.find_element("css selector",link).click()
                    try:
                        targets(list)
                        driver.back()
                    except:
                        driver.back()
                        try:
                            driver.find_element("css selector",link).click()
                            targets(list)
                            driver.back()
                        except:
                            targets(list)
                            driver.back()
                except:
                    break
            driver.find_element("css selector","body > div.content > div.mainContentContainer > div.mainContent > div.mainContentFloat > div.leftContainer > div.right > div > a.next_page").click()

        with open(f'../Data/pickles/Book_{gen}.pkl', 'wb') as f:
            pickle.dump(list, f)
        list = []  

#Function that gets the first 5000 books of a popular list.

"""
This function takes a Goodreads book list URL, email, and password as inputs. It logs in to the Goodreads
website using the provided email and password, and then navigates through the pages of the book list,
scraping book information using the 'targets' function. The collected book information is stored in a list
and then saved to a pickle file.

Args:
- Book_list (str): The URL of the Goodreads book list.
- Email (str): The email address used for logging in to Goodreads.
- Password (str): The password used for logging in to Goodreads.

Returns:
- None
"""
def search_list(Book_list,Email,Password):
    list = []
    driver.get(Book_list)
    driver.find_element("css selector","body > div.content > div.siteHeader > div > header > div.siteHeader__topLine.gr-box.gr-box--withShadow > div > ul > li:nth-child(1) > a").click()
    driver.find_element("css selector","#choices > div > a:nth-child(4) > button").click()
    driver.find_element("css selector","#ap_email").click()
    driver.find_element("css selector","#ap_email").send_keys(Email)
    driver.find_element("css selector","#ap_password").click()
    driver.find_element("css selector","#ap_password").send_keys(Password)
    driver.find_element("css selector","#signInSubmit").click()
    driver.implicitly_wait(30)
    for page in range (50):
        for i in range(1,101):
            try:   
                iterator = str(i)            
                link = "#all_votes > table > tbody > tr:nth-child("+iterator+") > td:nth-child(3) > a > span"
                driver.find_element("css selector",link).click()
                targets(list)
            except:
                pass

        driver.find_element("css selector","#all_votes > div.pagination > a.next_page").click()
    with open(f'../Data/pickles/Book_List.pkl', 'wb') as f:
        pickle.dump(list, f)       
#Cleaning the scraped books from Goodreads.
"""
Cleans and processes book data from multiple genres and updates a Pandas DataFrame.

Args:
    book_genres (list): List of book genres.
    book_df (DataFrame): Pandas DataFrame to be updated with book data.

Returns:
    DataFrame: Updated Pandas DataFrame with cleaned book data.
"""
def book_cleaner(book_genres,book_df):
    book_list = []
    for gen in book_genres:
        with open(f"../Data/pickles/Book_{gen}.pkl", "rb") as alias:
            book = pickle.load(alias)
        book_list.append(book)
    for book_genre in book_list:
        book_genre = pd.DataFrame(book_genre)
        book_genre[6] = book_genre[6].apply(', '.join)
        book_genre.columns = ["Book_author","Book_img","Book_description","Book_rating","Book_votes","Book_title","Book_genre"]
        book_genre["Book_description"] = book_genre["Book_description"].apply(lambda x: book_description_cleaner(x))
        book_genre["Book_rating"] = book_genre["Book_rating"].apply(lambda x: book_rating_cleaner(x))
        book_genre["Book_votes"] = book_genre["Book_votes"].apply(lambda x: book_vote_cleaner(x))
        book_genre["Book_genre"] = book_genre["Book_genre"].apply(lambda x: book_genres_cleaning(x))
        book_df = pd.concat([book_df,book_genre])
    return book_df
"""
Cleans a book rating by replacing "," with "." and converting it to a float.

Args:
    book_rating (str): Book rating to be cleaned.

Returns:
    float: Cleaned book rating.
"""
def book_rating_cleaner(book_rating):
    return float(book_rating.replace(",","."))

"""
Multiplies a book rating by a factor of 2.

Args:
    book_rating (float): Book rating to be multiplied.

Returns:
    float: Multiplied book rating.
"""
def book_rating_multiplier(book_rating):
    return book_rating*2

"""
Cleans a book genre by replacing "," with "|" and removing spaces.

Args:
    book_genre (str): Book genre to be cleaned.

Returns:
    str: Cleaned book genre.
"""
def book_genres_cleaning(book_genre):
    return book_genre.replace(",","|").replace(" ","")

"""
Cleans a book vote count by splitting the string at the first space, removing "," from the resulting string,
and converting it to an integer.

Args:
    book_vote (str): Book vote count to be cleaned.

Returns:
    int: Cleaned book vote count.
"""
def book_vote_cleaner(book_vote):
    book_vote_clean = book_vote.split(" ")[0].replace(",","")
    return int(book_vote_clean)
"""
Cleans a book description by replacing "\n" with a space.

Args:
    book_description (str): Book description to be cleaned.

Returns:
    str: Cleaned book description.
"""
def book_description_cleaner(book_description):
    return book_description.replace("\n"," ")


#Resources to scrap imdb:
"""
Scrapes movie data from IMDb website for a specific genre column on the IMDb genre page.

Args:
    n_col (int): The column number of the genre on the IMDb genre page (1-6).
    
Returns:
    None
"""
def search(n_col):
    list = []
    for num in range(1,7):
        driver.get("https://www.imdb.com/feature/genre/")
        num = str(num)
        genre = f"#main > div:nth-child(13) > span > div > div > div > div > div:nth-child({n_col}) > div > div:nth-child("+num+") > div > a"
        driver.find_element("css selector",genre).click()
        for pages in range(100):
            try:
                for movie in range(1,51):
                    driver.implicitly_wait(2)
                    inner = []
                    iterator = str(movie)
                    title_id = "#main > div > div.lister.list.detail.sub-list > div > div:nth-child("+iterator+") > div.lister-item-content > h3 > a"
                    poster_id = "#main > div > div.lister.list.detail.sub-list > div > div:nth-child("+iterator+") > div.lister-item-image.float-left > a > img"
                    genre_id = "#main > div > div.lister.list.detail.sub-list > div > div:nth-child("+iterator+") > div.lister-item-content > p:nth-child(2) > span.genre"
                    rating_id = "#main > div > div.lister.list.detail.sub-list > div > div:nth-child("+iterator+") > div.lister-item-content > div > div.inline-block.ratings-imdb-rating > strong"
                    description_id = "#main > div > div.lister.list.detail.sub-list > div > div:nth-child("+iterator+") > div.lister-item-content > p:nth-child(4)"
                    votes_id = "#main > div > div.lister.list.detail.sub-list > div > div:nth-child("+iterator+") > div.lister-item-content > p.sort-num_votes-visible > span:nth-child(2)"
                    director_casting_id = "#main > div > div.lister.list.detail.sub-list > div > div:nth-child("+iterator+") > div.lister-item-content > p:nth-child(5)"
                    try:
                        inner.append(driver.find_element("css selector",title_id).text)
                        inner.append(driver.find_element("css selector",poster_id).get_attribute("src"))
                        inner.append(driver.find_element("css selector",genre_id).text)
                        inner.append(driver.find_element("css selector",description_id).text)
                        inner.append(driver.find_element("css selector",rating_id).text)
                        inner.append(driver.find_element("css selector",director_casting_id).text)
                        inner.append(driver.find_element("css selector",votes_id).text)
                        list.append(inner)
                    except:
                        pass

                try:
                    driver.find_element("css selector","#main > div > div.desc > a.lister-page-next.next-page").click()           
                except:
                    try:
                        driver.find_element("css selector","#main > div > div.desc > a").click()
                    except:
                        break
            except:
                break

        with open(f'../Data/pickles/genre_{n_col}_{num}.pkl', 'wb') as f:
            pickle.dump(list, f)
        list = []


#Resources to clean imdb:
"""
Cleans and processes movie data from pickle files and adds it to a main dataframe.

Args:
    main_df (pandas DataFrame): Main dataframe to which the movie data will be added.

Returns:
    pandas DataFrame: Updated main dataframe with cleaned movie data.

"""
def movie_cleaner(main_df):
    lista = [f"genre_{x}" for x in range(1,7)] + [f"genre_{numb}_{n}" for numb in range(2,5) for n in range(1,7)]
    movie_list = []
    for movie_genero in lista:
        with open(f"../Data/pickles/{movie_genero}.pkl", "rb") as alias:
            genero_pelis = pickle.load(alias)
        movie_list.append(genero_pelis)
    for movies in movie_list:
        movie_df = pd.DataFrame(movies)
        movie_df.columns = ["Movie_name","Movie_img","Movie_genre","Movie_description","Movie_rating","Casting","Movie_votes"]
        movie_df["Movie_rating"] = movie_df["Movie_rating"].apply(lambda x: movie_rating_cleaner(x))
        movie_df["Movie_votes"] = movie_df["Movie_votes"].apply(lambda x: movie_vote_cleaner(x))
        movie_df["Movie_genre"] = movie_df["Movie_genre"].apply(lambda x: movie_genres_cleaning(x))
        movie_df["Movie_directors"] = movie_df["Casting"].apply(lambda x: movie_director(x))
        movie_df["Movie_stars"] = movie_df["Casting"].apply(lambda x: movie_stars(x))
        main_df = pd.concat([main_df,movie_df])
    return main_df

"""
Cleans movie rating by replacing commas with dots and converting it to float.

Args:
    movie_rating (str): Movie rating string.

Returns:
    float: Cleaned movie rating as a float.

"""
def movie_rating_cleaner(movie_rating):
    return float(movie_rating.replace(",","."))
"""
Cleans movie vote count by removing commas and converting it to an integer.

Args:
    movie_vote (str): Movie vote count string.

Returns:
    int: Cleaned movie vote count as an integer.

"""
def movie_vote_cleaner(movie_vote):
    try:
        try:
            movie_vote = movie_vote.replace(".","")
        except:
            movie_vote = movie_vote.replace(",","")
    except:
        pass
    return int(movie_vote)
"""
Extracts movie director(s) from movie casting string.

Args:
    movie_casting (str): Movie casting string.

Returns:
    str: Extracted movie director(s) as a string.

"""

def movie_director(movie_casting):
    if "Director" in movie_casting:
        if "Stars" in movie_casting:
            directores = movie_casting.split("|")[0].split(":")[1]
        else:
            directores = movie_casting.split(":")[1]
    else:
        directores = "No directors"
    return directores
"""
Extracts movie star(s) from movie casting string.

Args:
    movie_casting (str): Movie casting string.

Returns:
    str: Extracted movie star(s) as a string.

"""
def movie_stars(movie_casting):
    if "Stars" in movie_casting:
        if "Director" in movie_casting:
            actores = movie_casting.split("|")[1].split(":")[1]
        else:
            actores = movie_casting.split(":")[1]
    else:
        actores = "No stars"
    return actores
"""
Cleans movie genre string by replacing commas with pipes and removing spaces.

Args:
    movie_genre (str): Movie genre string.

Returns:
    str: Cleaned movie genre string.

"""
def movie_genres_cleaning(movie_genre):
    return movie_genre.replace(",","|").replace(" ","")
"""
Cleans movie casting string by replacing commas with pipes and removing spaces.

Args:
    movie_casting (str): Movie casting string.

Returns:
    str: Cleaned movie casting string.

"""
def split_casting(movie_casting):
    return movie_casting.replace(",","|").replace(" ","")

#Resources for Genre cleaning notebook:
"""
Maps movie genre string to corresponding genre codes using a dictionary.

Args:
    movie_genres (str): Movie genre string.

Returns:
    str or None: Mapped movie genre codes separated by pipes ('|') as a string, or None if no genre codes are mapped.

"""
def map_genre(movie_genres):
    genres_list = movie_genres.split('|')

    genres_mapped = list(set(map(lib.Book_genre_dic.get, genres_list)))

    if "Drop" in genres_mapped:
        genres_mapped.remove("Drop")

    genres_mapped = '|'.join([genre for genre in genres_mapped if genre is not None])

    return genres_mapped if genres_mapped else None

"""
Cleans a string by removing any numeric digits.

Args:
    argum (str): Input string to be cleaned.

Returns:
    str: Cleaned string with numeric digits removed.

"""
def num_cleaner(argum):
    s = argum.lower()
    s= re.sub(r"\d+","", s)
    return s

"""
Generates combinations of tokens from a string of genre names separated by pipes ('|').

Args:
    gen (str): Input string containing genre names separated by pipes ('|').

Returns:
    list: List of combinations of tokens, each prefixed with "Genre -", sorted in alphabetical order.

"""
def token_gen(gen):
    gen_sep = gen.split("|")
    outcome = []
    for size in [1,2]:
        combs = ["Genre -" + "|".join(sorted(tup))
            for tup in combinations(gen_sep,r=size)]
        outcome = outcome + combs
    return sorted(outcome)

"""
Function to create a similarity matrix for recommendation using cosine similarity.

Parameters:
-- df: pandas DataFrame
    Input DataFrame containing the data for which the similarity matrix needs to be created.
    It should contain the following columns:
        - "Title_id": Unique identifier for each title.
        - "Description": Text description for each title.
        - "Genre": Genre information for each title.

Returns:
-- None

Saves the following pickles:
    - Ord_matrix.pkl: Pickle file containing the ordered indices of titles based on cosine similarity.
    - Cos_sim_matrix.pkl: Pickle file containing the cosine similarity values for each pair of titles.

"""
def matrix(df):
    counter_args = CountVectorizer(preprocessor = num_cleaner,
                               min_df = 7)
    
    args_bag_of_words = (counter_args
                     .fit_transform(df["Description"])
                     .toarray()
                     )
    col_args = [tup[0] for tup in
            sorted(counter_args.vocabulary_.items(),
                   key=lambda x: x[1])]
    args_bag_of_words_df = pd.DataFrame(args_bag_of_words,
                                 columns=col_args,
                                 index = df["Title_id"])
    counter_genre = CountVectorizer(tokenizer=token_gen,
                                token_pattern=None,
                                lowercase=False)
    counter_genre.fit(df["Genre"])
    genre_bag_of_words = counter_genre.fit_transform(df["Genre"]).toarray()
    col_genre = [tup[0] for tup in
             sorted(counter_genre.vocabulary_.items(),
                    key=lambda x: x[1])]
    genre_bag_of_words_df = pd.DataFrame(genre_bag_of_words,
                                     columns=col_genre,
                                     index=df["Title_id"])
    bag_of_words_final = np.hstack((args_bag_of_words,genre_bag_of_words))
    bag_of_words_final_df = pd.DataFrame(bag_of_words_final,
                                     columns = col_args+col_genre,
                                     index=df["Title_id"])
    tf_idf = TfidfTransformer()
    tf_idf_recomend = tf_idf.fit_transform(bag_of_words_final_df).toarray()
    tf_idf_recomend_df = pd.DataFrame(tf_idf_recomend,
                               index = df["Title_id"],
                               columns = col_args+col_genre)
    cosine_sims = cosine_similarity(tf_idf_recomend_df)

    matrix_sim_df = pd.DataFrame(cosine_sims,
                                 index=df["Title_id"],
                                 columns=df["Title_id"])
    np.fill_diagonal(matrix_sim_df.values,np.nan)

    ord_matrix = np.argsort((-cosine_sims), axis=1)
    cos_sim_ord = np.sort(-cosine_sims,axis=1)

    with open(f'../Data/pickles/Ord_matrix.pkl', 'wb') as f:
        pickle.dump(ord_matrix, f)
    with open(f'../Data/pickles/Cos_sim_matrix.pkl', 'wb') as f:
        pickle.dump(cos_sim_ord, f)



"""
Function to retrieve top recommendations for a given title based on precomputed similarity matrix.

Parameters:
-- name: str
    Name of the title for which recommendations need to be generated.

Returns:
-- top_k_df: pandas DataFrame
    DataFrame containing the top recommended titles based on precomputed similarity matrix.
    It contains the following columns:
        - "Title": Title names of the recommended titles.
        - "Description": Text descriptions of the recommended titles.
        - "Genre": Genre information of the recommended titles.
        - "similarity": Cosine similarity scores of the recommended titles with the input title.
"""
def top(name):
    df = pd.read_csv("../Data/recomendation.csv",index_col=0)
    with open(f"../Data/pickles/Cos_sim_matrix.pkl", "rb") as alias:
        cos_sim_matrix = pickle.load(alias)
    with open(f"../Data/pickles/Ord_matrix.pkl", "rb") as alias:
        ord_matrix = pickle.load(alias)
    indice = df.loc[df["Title"] == name].index[0]
    ord_list_sim = ord_matrix[indice]
    ord_list_sim2 = cos_sim_matrix[indice]

    top_k = ord_list_sim[:20]
    cosine_sims_top_k = ord_list_sim2[:20]
    
    top_k_df = df.loc[top_k].copy()
    top_k_df["similarity"] = cosine_sims_top_k
    return top_k_df 

