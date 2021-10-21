"""
package untuk bs
"""
from bs4 import BeautifulSoup
import requests




def ngambil_data():
    global hasil
    headers = {
        'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }
    detik = requests.get('https://www.detik.com/', headers= headers)
    if detik.status_code == 200:
        soup = BeautifulSoup(detik.content,    "html.parser")
        satu = soup.find('a', {'dtr-evt': 'box artikel terpopuler', 'dtr-idx': '1'})['dtr-ttl']
        dua = soup.find('a', {'dtr-evt': 'box artikel terpopuler', 'dtr-idx': '2'})['dtr-ttl']
        tiga = soup.find('a', {'dtr-evt': 'box artikel terpopuler', 'dtr-idx': '3'})['dtr-ttl']
        empat = soup.find('a', {'dtr-evt': 'box artikel terpopuler', 'dtr-idx': '4'})['dtr-ttl']
        lima = soup.find('a', {'dtr-evt': 'box artikel terpopuler', 'dtr-idx': '5'})['dtr-ttl']


        hasil = dict()
        hasil['satu'] = satu    #'Tanda Tanya Terjawab Soal Corona Global Turun tapi Menggila di Eropa'
        hasil['dua'] = dua      #'Denmark Open 2021: Pemain Top Rontok, Juara Olimpiade 2020 Tersingkir'
        hasil['tiga'] = tiga    #'Pengakuan Tersangka Pinjol Ilegal yang Sebabkan Ibu di Wonogiri Gantung Diri'
        hasil['empat'] = empat  #'Adam Deni Ngaku Ditawari Miliaran Rupiah agar Cabut Laporan ke Jerinx'
        hasil['lima'] = lima    #'Novel Baswedan dkk Kembali Laporkan Lili Pintauli ke Dewas KPK!'
    return hasil


def nampil_data(result):
    print('Trend Berita DI detik.com: ')
    print(f"Pertama:  {result['satu']}")
    print(f"Kedua:    {result['dua']}")
    print(f"Ketiga:   {result['tiga']}")
    print(f"Kempat:   {result['empat']}")
    print(f"Kelima:   {result['lima']}")

if __name__ == '__main__':
    print('ini utama')
