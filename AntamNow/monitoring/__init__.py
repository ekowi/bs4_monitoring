"""
Now this time ill try scrapping data from e-commerece
"""

import requests
from bs4 import BeautifulSoup
import json

def get_data():
    url = requests.get('https://harga-emas.org/')
    data = url.text
    soup = BeautifulSoup(data,  'html.parser')
    table = soup.findAll('table', {'class': 'in_table', 'style': 'padding-top: 15px;'})
    for i in table:
        print(i.text)




def show_data(result):
    pass
