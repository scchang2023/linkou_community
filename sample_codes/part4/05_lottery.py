import requests
from bs4 import BeautifulSoup

html=requests.get("https://www.taiwanlottery.com.tw/result_all.htm")
html.encoding="utf-8"
bs=BeautifulSoup(html.text,"html.parser")
divs=bs.find_all("div", {"class":"intx01"})
tds=divs[1].find_all("td",{"class":"even"}) 
spans=tds[4].find_all("span")
print("依大小順序：",end="")
for i in range(0,6):
    print(spans[i].text,end=" ")
print("\n依開出順序：",end="")
for i in range(8,14):
    print(spans[i].text,end=" ")
print("\n特別號：",spans[7].text)