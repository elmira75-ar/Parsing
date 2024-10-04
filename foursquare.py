# Напишите сценарий на языке Python, который предложит пользователю 
# ввести интересующую его категорию (например, кофейни, музеи, парки и т.д.).
# Используйте API Foursquare для поиска заведений в указанной категории.
# Получите название заведения, его адрес и рейтинг для каждого из них.
# Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль.


# python -m pip install requests
# import requests
# url = "https://api.foursquare.com/v3/places/search"
# headers = {"accept": "application/json"}
# response = requests.get(url, headers=headers)
# print(response.text)

import os
import requests
import json
from dotenv import load_dotenv
from pprint import pprint

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Ваши учетные данные API
api_key = os.getenv("a_k")
client_id = os.getenv("c_id")
client_secret = os.getenv("c_secret")

# Конечная точка API
endpoint = "https://api.foursquare.com/v3/places/search"

# Определение параметров для запроса API
city = input("Введите название города: ")
params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "near": city,
    "query": "restaurant"
    # "query": category
}

headers = {
    "Accept": "application/json",
    "Authorization": api_key
}

# Отправка запроса API и получение ответа
response = requests.get(endpoint, params=params,headers=headers)

# Проверка успешности запроса API
if response.status_code == 200:
    print("Успешный запрос API!")
    data = json.loads(response.text)
    venues = data["results"]
    # pprint(venues)
    # for venue in venues:
    #     for k,v in venue.items():
    #         print(k,v)
    #         print("\n")
    for venue in venues:
        print("Название:", venue["name"])
        # print("Категория:", venue.get("categories")["plural_name"]) # dict.get(key)
        print("Адрес:", venue["location"]["address"])
        print("\n")
else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)
