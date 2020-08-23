import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')

# Using CSS Selectors

print(soup.select('a'))
print(soup.select('div'))
print(soup.select('.score'))
print(soup.select('#score_24245817'))
links = soup.select('.storylink')
votes = soup.select('.score')
print(votes[0])
print(votes[0].get('id'))
