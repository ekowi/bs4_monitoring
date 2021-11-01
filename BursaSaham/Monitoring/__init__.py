from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime
def ambildata():
    global hasil
    url = 'https://id.tradingeconomics.com/indonesia/stock-market'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/95.0.4638.54 Safari/537.36'
    }
    link = requests.get(url, headers=headers)
    if link.status_code == 200:
        soup = BeautifulSoup(link.text,     'html.parser')
        bca = soup.find('tr', {'data-decimals': '2', 'data-symbol': 'BBCA:IJ'}).findChildren('td')[2].text
        bcatahun = soup.find('tr', {'data-decimals': '2', 'data-symbol': 'BBCA:IJ'}).findChildren('td')[6].text
        bri = soup.find('tr', {'data-decimals': '2', 'data-symbol': 'BBRI:IJ'}).findChildren('td')[2].text
        britahun = soup.find('tr', {'data-decimals': '2', 'data-symbol': 'BBRI:IJ'}).findChildren('td')[6].text
        bmri = soup.find('tr', {'data-decimals': '2', 'data-symbol': 'BMRI:IJ'}).findChildren('td')[2].text
        bmritahun = soup.find('tr', {'data-decimals': '2', 'data-symbol': 'BMRI:IJ'}).findChildren('td')[6].text

        hasil = dict()
        hasil['bca'] = bca
        hasil['bcatahun'] = bcatahun
        hasil['bri'] = bri
        hasil['britahun'] = britahun
        hasil['bmri'] = bmri
        hasil['bmritahun'] = bmritahun
    else:
        print('internet terputus')
    return hasil


def tampildata(result):
    # print(f"data saham bca adalah {result['bca']}")
    # print(f"Perbandingan Tahun lalu {result['bcatahun']}")
    # print(f"data saham bri adalah {result['bri']}")
    # print(f"Perbandingan Tahun lalu {result['britahun']}")
    # print(f"data saham mandiri adalah {result['bmri']}")
    # print(f"Perbandingan Tahun lalu {result['bmritahun']}")
    print(f"{result['bca']}")
    print(f"{result['bcatahun']}")
    print(f"{result['bri']}")
    print(f"{result['britahun']}")
    print(f"{result['bmri']}")
    print(f"{result['bmritahun']}")
    with open('index.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        # writer.writerow([f"{'BCA' : ^20}", f"{'Tahun Lalu' : ^20}",
        #                  f"{'BRI' : ^20}", f"{'Tahun Lalu' : ^20}",
        #                  f"{'MANDIRI' : ^20}", f"{'Tahun Lalu' : ^20}", f"{'Waktu' : ^20}"])
        writer.writerow([f"{result['bca']}", f"{result['bcatahun']}",
                         f"{result['bri']}", f"{result['britahun']}",
                         f"{result['bmri']}", f"{result['bmritahun']}", datetime.now()])
    return result


if __name__ == '__main__':
    print('ini module monitoring')
