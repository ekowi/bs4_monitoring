# Import library first for html reader then import beatifulsoup4 then parser
# Hope this project will done in this february
import requests
from bs4 import BeautifulSoup
import json
import csv


# add variable for url search and headers
city = 'Depok'  #ex 'cibinong'
check_in = 'checkIn=26-01-2022&'   #dd-mm-yyyy
check_out = 'checkOut=26-02-2022&'  #dd-mm-yyyy
list = []
# Get data from link
def get_data():
    url = 'https://www.travelio.com/newGetHotelByCriteria'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/97.0.4692.99 Safari/537.36"
    }
    payload = {
        'page': 1,
        'stayDurationType': 'monthly',
        'destinationId': '546c9db1b094a31e06e08a6b',
        'destinationCategory': 'city',
        'destination': 'Depok',
        'numberOfRooms': '1',
        'numberOfNights': '365',
        'formattedCheckinDate': '20220214',
        'breakfast': '0',
        'provider': 'all',
        'sortBy': 'default',
        'sortOrder': '1',
        'bottomPrice': '833333.6000000001',
        'upperPrice': '15523333.6',
        'instant': '0',
        'filterPropertyType' : None,
        'unitType' : None,
        'sellType' : None,
        'numberOfGuests': '1'
    }
    try:
        source = requests.post(url,  headers= headers, data=payload)
    except Exception:
        return None
    if source.status_code == 200:
        print(source.status_code)
        soup = BeautifulSoup(source.text,   'html.parser')
        data_json = json.loads(soup.text)
        data = data_json['data']
        global latitude, langtitude
        for nama in data:
            hotel = nama['building']['name']
            price_month = nama['displayMonthlyPrice']
            i = 0
            for dat in nama['loc']['coordinates']:
                i += 1
                if i % 2 == 0:
                    latitude = dat
                else:
                    langtitude = dat



            data_lokasi = {
                'latitude' : latitude,
                'langtitude' : langtitude
                    }
            data_dict = {
                        'nama' : hotel,
                        'harga' : price_month,
                        'lokasi' : data_lokasi,
                       }
            list.append(data_dict)









def tampil_data(data):
    print('ini batas')
    print(list)
    return data
