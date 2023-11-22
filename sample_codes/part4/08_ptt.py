import requests
from bs4 import BeautifulSoup

html=requests.get("https://www.ptt.cc/bbs/CarShop/index.html")
bs=BeautifulSoup(html.text,"html.parser")
divs=bs.find_all("div",{"class":"r-ent"})
for div in divs:
    a=div.find("a")
    if a==None or "公告" in a.text:
        continue    
    href=a.get("href")
    href="https://www.ptt.cc/"+href
    html1=requests.get(href)
    bs1=BeautifulSoup(html1.text,"html.parser")
    bs2=bs1.find("div",{"id":"main-container"})
    print(a.text)
    print(bs2.text)
