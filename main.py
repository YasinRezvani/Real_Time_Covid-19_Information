import requests
import re
import time
from bs4 import BeautifulSoup as bs
from beautifultable import BeautifulTable

table = BeautifulTable()
country = input("\n Enter Country: ").lower()
url = "https://www.worldometers.info/coronavirus/country/" + country
req = requests.get(url)
scrap = bs(req.content , "html.parser")
data = scrap.find_all("div" , {"class" : "maincounter-number"} , "span")
list = []