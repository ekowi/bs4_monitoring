"""
this time i will try twitter trend for learn scrappy data from website
"""

import requests
from bs4 import BeautifulSoup
import re

# def funtion for acsess data from website
def get_data():
    url = 'https://covid19.go.id/'
    headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/95.0.4638.69 Safari/537.36'
    }
    try:
        source = requests.get(url, headers= headers)
    except Exception:
        return None
    if source.status_code == 200:
        soup = BeautifulSoup(source.text,   'html.parser')
        hasil = soup.find('div', {'class' : 'col-md-3 text-color-black p-4',
                                  'style' : 'background-color: rgb(234, 104, 82);'})
        nilai = hasil.findAll('strong')
        i = 0
        positif = 0
        sembuh = 0
        meninggal = 0
        for has in nilai:
            i = i + 1
            if i == 1:
                positif = has.text
            if i == 2:
                sembuh = has.text
            if i == 3:
                meninggal = has.text

        update = hasil.find('div', {'class' : 'pt-4 text-color-black text-1'}).text

        hasil = dict()
        hasil['positif'] = positif
        hasil['sembuh'] = sembuh
        hasil['meniggal'] = meninggal
        hasil['update'] = update
    return hasil


def tampildata(result):
    print(f"Jumlah orang yang Positif covid19 {result['positif']}")
    print(f"Jumlah orang yang Sembuh dari covid19 {result['sembuh']}")
    print(f"Jumlah orang yang Meninggal karna covid19 {result['meniggal']}")
    print(f"{result['update']}")




