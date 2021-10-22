"""
Now this time ill try scrapping data from e-commerece
"""

import requests
from bs4 import BeautifulSoup
import json

def get_data():
    keyword = 'xiaomi'
    url = requests.get(f'https://www.jd.id/search?keywords={keyword}')
    data = url.text
    soup = BeautifulSoup(data,  'html.parser')
    json = soup.findAll('script')
    print(json)


def show_data(result):
    pass
