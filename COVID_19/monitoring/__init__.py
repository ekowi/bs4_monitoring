"""
this time i will try twitter trend for learn scrappy data from website
"""

import requests
from bs4 import BeautifulSoup
import re

# def funtion for acsess data from website
def get_data():
    keyword = 'indonesia'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/94.0.4606.81 Safari/537.36'
    }
    url = requests.get(f'https://www.worldometers.info/coronavirus/country/{keyword}/', headers=headers)

    soup = BeautifulSoup(url.text,    'html.parser')
    infected = soup.findAll('div', {'id': 'maincounter-wrap'})
    for i in infected:
        data = i.text
        data = re.sub('\n', '', data)
        data = re.sub('Daily Cases Graph - Daily Deaths Graph', '', data)
        print(data)
    return data



