from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pickle
import warnings
warnings.filterwarnings('ignore')
driver = webdriver.Chrome(ChromeDriverManager().install())

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

