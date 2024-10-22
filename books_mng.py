# Загрузите данные которые вы получили
# на предыдущем уроке путем скрейпинга
# сайта с помощью Beautiful Soup в MongoDB
# и создайте базу данных и коллекции для их хранения. 

import json
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client["scraping"]
collection = db["books"]
 
with open('books_as_json.json') as file:
    file_data = json.load(file)
     
collection.insert_one(file_data) 

query = {"name" : "Shakespeare's Sonnets"}

results = db.books.find(query)
for a in results:
    print(a)