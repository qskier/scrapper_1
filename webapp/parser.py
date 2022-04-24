import requests
from bs4 import BeautifulSoup as bs

import settings

url = settings.URL_PARSER
request = requests.get(url)
soup = bs(request.text, 'html.parser')

flats = soup.find('b')
#print(flats)
#print(len(flats))

flats = flats.contents[0]
flats = flats.split(" ")
flats = flats[0]


print(type(flats)) 
print(flats)
#print(flats[0])




#flats = soup.find_all('class' = "b-search-filter__counter j-search-filter-counter")
#flats = soup.find('div', class_='b-search-filter__counter j-search-filter-counter')
 #print soup.find('a').contents[0]
 #firststansbot 