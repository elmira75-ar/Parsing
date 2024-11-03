from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import csv
 

url = 'https://books.toscrape.com/'
driver = webdriver.Chrome()
driver.get(url)                                               
driver.implicitly_wait(10)                                                              

titles, prices, rating, stock = [], [], [], []                                          
ratings = {'One': 1, 'Two': 2, 'Three': 3, 'Four' : 4, 'Five': 5}                       
books_lst = {'name':titles, 'price': prices, 'rating':rating, 'in_stock':stock}

# pages =  int(driver.find_element(By.XPATH, "//li[@class='current']").text[-2:])
# for page in range(1, pages + 1):
   
for page in range(1, 3):                                                      
    html = BeautifulSoup(driver.page_source, 'html.parser')                             
    books = html.find_all('li', {'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})       

    for book in books:                                                                  
        titles.append(book.find('h3').find('a').get('title'))                           
        prices.append(book.find('p', {'class': 'price_color'}).string)                  
        rating.append(ratings[book.find('p').get('class')[1]])                          
        stock_ = book.find(class_='instock availability').text.strip()
        # stock_ = book.find(class_='instock availability').text[-2]

        stock.append(stock_)

    next_page = driver.find_element(By.XPATH, "//a[contains(text(), 'next')]")
    next_page.click()                                                                   

# print(type(books_lst))

df = pd.DataFrame(books_lst)
df.to_csv('books.csv')

driver.close()
                                                      