import requests
from bs4 import BeautifulSoup

html=requests.get("https://invoice.etax.nat.gov.tw/")
bs=BeautifulSoup(html.text,"html.parser")
tables=bs.find_all("table")
reds=tables[0].find_all("span",{"class":"font-weight-bold etw-color-red"})
for red in reds:
    print(red.text)