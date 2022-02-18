# Import library first for html reader then import beatifulsoup4 then parser
# Hope this project will done in this february
import requests
from bs4 import BeautifulSoup
import json
import os
import pandas as pd


#run this funtion to get data from other page and date
def run():
    pass

list = []
# Get data from link
def get_data(page, date):
    url = 'https://www.travelio.com/newGetHotelByCriteria'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/97.0.4692.99 Safari/537.36"
    }
    payload = {
        'page': page,
        'stayDurationType': 'monthly',
        'destinationId': '580740cad0746fa20a5a3f74',
        'destinationCategory': 'area',
        'destination': 'Kuningan',
        'numberOfRooms' : '1',
        'numberOfNights': '365',
        'formattedCheckinDate': date,
        'breakfast': '0',
        'provider': 'all',
        'sortBy': 'default',
        'sortOrder': '1',
        'bottomPrice': '2876608.8000000003',
        'upperPrice': '64996608.8',
        'instant': '0',
        'unitType': None,
        'sellType': None,
        'numberOfGuests': '1'
    }

    try:
        source = requests.post(url,  headers= headers, data=payload)
    except Exception:
        return None

    if source.status_code == 200:
        soup = BeautifulSoup(source.text,   'html.parser')
        data_json = json.loads(soup.text)
        data = data_json['data']

#Get data from link the parse data and cleaning data
        global latitude, langtitude, bed
        for nama in data:
            hotel = nama['building']['name']
            price_month = nama['displayMonthlyPrice']
            rating = nama['rating']
            room_max = nama['roomCapacity']
            book_date = nama['availStartDate']

            for i in nama['rooms']:
                bed = i['bedConfig']

            i = 0
            for dat in nama['loc']['coordinates']:
                i += 1
                if i % 2 == 0:
                    latitude = dat
                else:
                    langtitude = dat

#after data filled, add data to variable
            data_lokasi = {
                'latitude' : latitude,
                'langtitude' : langtitude
                    }
            data_dict = {
                        'nama' : hotel,
                        'max_tamu' : room_max,
                        'kasur' : bed,
                        'harga' : price_month,
                        'rating' : rating,
                        'lokasi' : data_lokasi,
                        'tersedia' : book_date
                       }
#then use list to make data global/ out from function
            list.append(data_dict)



#run this funtion to make csv or excel output
def panda(Dataframe):
    df = pd.DataFrame(Dataframe)
    df.to_csv(f"result/hasil.csv", index=False)
    df.to_excel(f"result/hasil.xlsx", index=False)



#run this funtion to make JSON output
def tampil_data(data):
    try:
        os.mkdir('result')
    except FileExistsError:
        pass
    if len(list) > 1 :
        with open(f"result/data_hotel.json", 'w+') as path:
            json.dump(list, path)
            print(f"data terkumpul sebanyak {len(list)} dan file json sudah jadi")
    else:
        print('data sudah habis coba halaman depan')

    return data



def run():
    page = input('Masukan Halaman yang diinginkan : ')
    date = input('Masukan tanggal booking hotel (YYYYMMDD) :')

    data = get_data(page,date)
    panda(list)
    tampil_data(data)

