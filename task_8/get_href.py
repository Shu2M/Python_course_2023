import requests
from bs4 import BeautifulSoup as bs
import csv

URL = 'https://soware.ru/categories/clients-and-partners-search-services'
res = requests.get(URL)
if not res.ok:
    raise Exception()

soup = bs(res.text, 'html.parser')

data = []

for a_teg, small_teg in zip(soup.find_all('a', {'class': 'dEWdHg'}), soup.find_all('a ~ small')):
    data.append(['https://soware.ru/'+a_teg['href'], small_teg.text.strip()])


with open('data.csv', 'w') as csv_file:
    write = csv.writer(csv_file)
    write.writerow(['Href', 'Partner'])
    write.writerows(data)


print(data)