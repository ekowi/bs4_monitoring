from bs4 import BeautifulSoup
import requests

def get_data():
    global data
    url = 'https://glints.com/id/opportunities/jobs/explore?keyword=it+support&country=ID&locationName=Indonesia'

    headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    try:
        contents = requests.get(url,   headers= headers)
    except Exception:
        return print('cek url')
    if contents.status_code == 200:
        soup = BeautifulSoup(contents.text,     'html.parser')
        title = soup.findAll('h3')
        pt = soup.findAll('a')
        print(pt)
        for list in title:
            title = list.text








            data = {
                'judul' : title
            }
            print(data)
    else:
        print('website tidak ditemukan')


def show_data(hasil):
    print(data)


get_data()