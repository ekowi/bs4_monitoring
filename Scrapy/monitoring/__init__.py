"""
package untuk bs
"""
from bs4 import BeautifulSoup
import requests
import requests




def ngambil_data():
    twitter = requests.get('https://twitter.com/i/trends')
    soup = BeautifulSoup(twitter.content,    "html.parser")
    trend = soup.find('span', 'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0')
    return trend


def nampil_data(result):
    pass

if __name__ == '__main__':
    print('ini utama')
