# The Art of Storytelling: A Collision of Cinema and the Literary World
![Sauron](Images/Book2.jpg)
---

<h1>Introduction</h1>

This project is an evolution of a [previous work](https://github.com/Slivered/Proyecto_ETL) where I compared the top 1000 movies from IMDB to their book counterparts, this time I expanded this project and decided to get as much information as possible for movies and books and analyze the data to make graphs, get some conclusions and as well do a recommend system using some machine learning technics.

<h2>Why?</h2>

---

* I have always loved reading as well as watching movies, so naturally I often compare movies and books together, wondering what's better and what are the strengths and weaknesses of these two worlds.

* As well, this is my final project in [Ironhack](https://www.ironhack.com/es/en/madrid?utm_campaign=MAD_Spain_Madrid_Global_Search_Brand_EN&utm_source=google&utm_medium=cpc&utm_content=search-brand&utm_term=ironhack&gad=1&gclid=CjwKCAjw6IiiBhAOEiwALNqnceab3m3h_XKvK9R8wBY9Fqe7wq2IQcXMBB4g97pWWAeFcBVMWjBJFhoCY_EQAvD_BwE) Data Analytics Bootcamp and I found it interesting to end the bootcamp with the same project as I started it, showcasing everything I have learned.

---

<h2>Objectives</h2>

* Get all the data by myself without using any starting csv.

* Be able to compare movies and books and see clearly what has usually better rating.

* Create a recomendation system using data scraped by myself.

* Showcase everything I did in a streamlit.


<h2>Methodology</h2>

---

* Data recollection 🔍

 I recollected the data using various Selenium functions to scrap Goodreads and imdb, these functions receive a list of genres that you desire and the function will scrap these genres for you, after each genre the data will be save in a .pkl file.



* Data treatment and cleaning 🧽

 I prepared various functions that will read a list of .pkl files transform them to DataFrames and clean them, then concat all of them together to have a single base DataFrame, then this DataFrame will go through various transformations.



* Analysis 🤓

 I used various visualization tools to make my graphs and as well some functions to make interactive filters to analyze and explore the data more deeply.


* Modeling 🖥

 And to end this project I did a recommendation system using machine learning techniques to give a recommendation based on the user input.
 

* Streamlit 📚

As well, I'll show my analysis, conclusions and model in a streamlit, it will be in Spanish as I'm presenting this project to a Spanish-speaking audience, but I'll make in the near future the same streamlit in English.


<h2>Thanks!!!!</h2>

I thank all of the Ironhack team but I specially want to thank:
* [Ana](https://www.linkedin.com/in/ana-garcia-garcia-090a5058/) for being the best teacher ever and having so much patience with me and Lin.
* [Jean-Charles](https://www.linkedin.com/in/jeancharlesyamada/) for the classes you taught us and help me get through this last project.
* [Cesar](https://www.linkedin.com/in/cesar-valle-iturriaga/) for allways being there to answer any questions we had.

<h2>Tools:</h2>

* [Pandas](https://pandas.pydata.org/docs/) is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.
* [Numpy](https://numpy.org/doc/stable/) is the fundamental package for scientific computing in Python.
* [Pickle](https://docs.python.org/3/library/pickle.html) is used to store safely a list outside of your notebook, so if your kernel shuts down you won't lose any data.
* [Selenium](https://www.selenium.dev/documentation/webdriver/) is a web scraping tool and it's great for automating your webscraping
* [Getpass](https://docs.python.org/3/library/getpass.html) is used to hide your mysql password.
* [Matplotlib](https://matplotlib.org/stable/index.html) was used to make the graphs.
* [PandasProfiling](https://ydata-profiling.ydata.ai/docs/master/index.html) primary goal is to provide a one-line Exploratory Data Analysis (EDA) experience in a consistent and fast solution. Like pandas df.describe() function, that is so handy, pandas-profiling delivers an extended analysis of a DataFrame while alllowing the data analysis to be exported in different formats such as html and json.