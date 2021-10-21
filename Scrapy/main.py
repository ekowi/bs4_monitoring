"""
kali ini akan belajar menarik data covid dari detik.com
menggunakan package beautiful soup 4 untuk scrapy data dan request untuk link
"""
from monitoring import ngambil_data, nampil_data

if __name__ == '__main__':
    print('ini aplikasi utama')
    result = ngambil_data()
    nampil_data(result)
