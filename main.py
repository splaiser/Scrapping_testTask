import requests
from bs4 import BeautifulSoup
from pprint import pprint

KEYWORDS = ['дизайн', 'фото', 'web', 'python',]

url = "https://habr.com/ru/all/"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
                         "537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.31"}
response = requests.get(url=url, headers=HEADERS).text
soup = BeautifulSoup(response, 'html.parser')
articles = soup.find_all('article')

for article in articles:
    text = article.find(class_="tm-article-snippet").text
    for word in KEYWORDS:
        if word.lower() in text.lower():
            date = article.find('time').attrs['title']
            name = article.find(class_='tm-article-snippet__title-link').text
            link = article.find(class_='tm-article-snippet__title-link').attrs['href']
            print(f"{date} - {name} - {url[:-8]}{link}")