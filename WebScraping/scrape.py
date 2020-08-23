import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)
print(soup.body)
print(soup.body.contents)
print(soup.find_all('div'))
print(soup.find_all('a'))
print(soup.title)
print(soup.a)
print(soup.find('a'))
print(soup.find(id='score_24245817'))

