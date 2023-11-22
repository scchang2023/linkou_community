import requests
from bs4 import BeautifulSoup

html=requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")
bs=BeautifulSoup(html.text,"html.parser")
table=bs.find("table",{"title":"牌告匯率"})
tbody=table.find("tbody")
trs=tbody.find_all("tr")
for tr in trs:
    tds=tr.find_all("td")
    currency_name=tds[0].find("div",{"class":"visible-phone"}).text
    currency_name=currency_name.replace("\r","")
    currency_name=currency_name.replace("\n","")
    currency_name=currency_name.replace(" ","")
    currency_rate=tds[2].text
    print(currency_name, currency_rate)
#6-9行可改寫為
#for tr in bs.find("table", {"title":"牌告匯率"}).find("tbody").find_all("tr"):
#12-14行可改寫為
#currency_name=currency_name.strip()
