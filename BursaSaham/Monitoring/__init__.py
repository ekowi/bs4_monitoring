from bs4 import BeautifulSoup
import requests

def ambildata():
    url = 'https://id.tradingeconomics.com/indonesia/stock-market'
    headers ={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/95.0.4638.54 Safari/537.36'
    }
    link = requests.get(url, headers=headers)
    soup = BeautifulSoup(link.text,     'html.parser')
    bca = soup.find('tr', {'data-decimals': '2', 'data-symbol': 'BBCA:IJ'}).text
    # bca = bca.strip().split('\n')

    hasil = dict()
    hasil['bca'] = bca
    return hasil




def tampildata(result):
    print(f"data saham bca adalah {result['bca']}")



    return result




if __name__ == '__main__':
    print('ini module monitoring')