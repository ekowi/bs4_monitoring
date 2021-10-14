"""
aplikasi monitoring covid 19 dari dtik.com
"""
import requests
from bs4 import BeautifulSoup




def ngambil_data():
    # """
    #                     indonesia   dunia
    # Kasus Positif	    4,232,099	240,021,219
    # Meninggal Dunia	    142,848	    4,891,285
    # Sembuh	            4,069,399	217,344,932
    # :return:
    # """
    content = requests.get('https://detik.com')

    if content == 200:
        soup = BeautifulSoup(content.text)
        print(soup.prettify())
    hasil = dict()
    hasil['positif'] = '4,232,099'
    hasil['meninggal'] = '142,848'
    hasil['sembuh'] = '4,069,399'
    return hasil


def nampil_data(result):
    print('Data Covid diindonesia via detik.com')
    print(f"Kasus Positif {result['positif']}")
    print(f"Meninggal Dunia {result['meninggal']}")
    print(f"Sembuh {result['sembuh']}")
    return



if __name__ == '__main__':
    result = ngambil_data()
    nampil_data(result)
