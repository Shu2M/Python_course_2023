import requests
from bs4 import BeautifulSoup as bs
import csv

# URL = 'https://dns-shop.ru/catalog/0985b00c0516c6ed/elektronnaya-cifrovaya-podpis/'
# # res = requests.get(URL)
# # if not res.ok:
# #     raise Exception()

with open('index.html', 'r', encoding="utf8") as index:
    soup = bs(index, 'html.parser')

with open('dns_shop.csv', 'w') as csv_file:
    write = csv.writer(csv_file)
    write.writerow(['Href', 'Code', "Name"])

    for div in soup.find_all('div', {'class': 'catalog-product'}):
        write.writerow([
            'https://dns-shop.ru/'+div.a['href'],
            div['data-code'],
            div.a.text
        ])
