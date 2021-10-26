from bs4 import BeautifulSoup
import requests

def ambildata():
    url = 'https://id.tradingeconomics.com/indonesia/stock-market'
    headers ={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/95.0.4638.54 Safari/537.36'
    }
    link = requests.get(url, headers=headers)
    if link.status_code == 200:
        soup = BeautifulSoup(link.text,     'html.parser')
        bca = soup.find('tr', {'data-decimals': '2', 'data-symbol': 'BBCA:IJ'}).findChildren('td')[2].text
        bcaTahun = soup.find('tr', {'data-decimals': '2', 'data-symbol': 'BBCA:IJ'}).findChildren('td')[6].text


        hasil = dict()
        hasil['bca'] = bca
        hasil['tahun'] = bcaTahun
    return hasil




def tampildata(result):
    print(f"data saham bca adalah {result['bca']}")
    print(f"Perbandingan Tahun lalu {result['tahun']}")



    return result




if __name__ == '__main__':
    print('ini module monitoring')