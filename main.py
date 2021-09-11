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

for i in data:
    regex = re.sub("\s+" , " " , i.text).strip()
    list.append(regex)

for i in list:
    table.rows.append([i])

table.columns.header = [country.title()]
table.rows.header = ["Coronavirus Cases:", "Deaths:", "Recovered:"]
table.set_style(BeautifulTable.STYLE_BOX_ROUNDED)
localtime = time.asctime(time.localtime(time.time()))
print("\n --- "+localtime+" ---")
print("")
print(table)
input()


# Made By Yasin Rezvani