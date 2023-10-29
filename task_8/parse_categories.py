import requests
from bs4 import BeautifulSoup as bs
import csv

URL = 'https://soware.ru/categories/reference'
res = requests.get(URL)
if not res.ok:
    raise Exception()

soup = bs(res.text, 'html.parser')

with open('categories.csv', 'w') as csv_file:
    write = csv.writer(csv_file)
    write.writerow(['Href', 'Category'])

    for a_teg in soup.find_all('a', {'class': 'dqvSXx'}):
        write.writerow(['https://soware.ru/'+a_teg['href'], a_teg.text.strip()])

