import requests
from bs4 import BeautifulSoup
import pprint  # preety printer

# for i in range(1, 3):  # Number of pages plus one
#     url = "https://news.ycombinator.com/news?p=" + str(i)

url1 = "https://news.ycombinator.com/news?p=1"
res1 = requests.get(url1)
soup1 = BeautifulSoup(res1.text, 'html.parser')
links1 = soup1.select('.storylink')
# votes = soup.select('.score')
subtext1 = soup1.select('.subtext')

url2 = "https://news.ycombinator.com/news?p=2"
res2 = requests.get(url2)
soup2 = BeautifulSoup(res2.text, 'html.parser')
links2 = soup2.select('.storylink')
# votes = soup.select('.score')
subtext2 = soup2.select('.subtext')

mega_link = links1 + links2
mega_subtext = subtext1 + subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)

        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            # print(points)
            if points > 100:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_link, mega_subtext))
