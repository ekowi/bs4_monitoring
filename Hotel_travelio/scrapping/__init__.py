# Import library first for html reader then import beatifulsoup4 then parser
# Hope this project will done in this february
import requests
from bs4 import BeautifulSoup


# add variable for url search and headers
city = 'Depok'  #ex 'cibinong'
check_in = 'checkIn=26-01-2022&'   #dd-mm-yyyy
check_out = 'checkOut=26-02-2022&'  #dd-mm-yyyy
url = f"https://www.travelio.com/search?searchType=monthly&destinationCategory=City&destinationUrlName=&" \
      f"destinationPlaceId=&destinationCountryId=ID&destinationId=546c9db1b094a31e06e08a6b&nights=31&flexible=1&" \
      f"destination={city}&{check_in}{check_out}months=1&cbFlexible=on&unitType=3%2C2%2C1%2Cstudio&" \
      f"propTypeId=guesthouse%2Chostel%2Chotel%2Croom%2Cvilla%2Chouse%2Capartment&" \
      f"sellType=Unfurnished%2CFull%2BFurnished&bottomPrice=833333.6000000001&upperPrice=15523333.6"
headers = {
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}

# Get data from link
tampil = requests.get(url)
print(tampil.status_code)

soup = BeautifulSoup(tampil.text,   'html.parser')
print(soup.prettify())
