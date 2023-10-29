import requests
from bs4 import BeautifulSoup as bs

URL = ''
res = requests.get(URL)
if not res.ok:
    raise Exception()

soup = bs(res.text, 'html.parser')

soup.find_all('div')
soup.find_all('div', {'class': 'class_name', 'id': 'id_name'})

soup.find('div')
soup.find('disfse')

soup.select('div')
soup.select_one('div')

soup.select('div.class_name')
soup.select('.class_name')

soup.select('div#id_name')
soup.select('#id_name')

soup.select('[href]')
soup.select('[href="https://..."]')

soup.select('div a')
soup.select('div div p')

soup.select('div > a')
soup.select('div > div > h')

soup.select('h1 ~ span')

h1 = soup.h1

h1_ = soup.h1.a

p = soup.div.p[0]

