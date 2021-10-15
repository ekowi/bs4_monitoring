"""
package untuk bs
"""
from bs4 import BeautifulSoup
import requests
import html5lib

soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

def ngambil_data():
    soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
    print(soup.prettify())
    return soup

def nampil_data(result):
    pass

if __name__ == '__main__':
    print('ini utama')
