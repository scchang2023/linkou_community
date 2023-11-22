import requests

url=input("請輸入您要搜尋的網址:")
html=requests.get(url)
html.encoding="utf-8"
htmllist=html.text.splitlines()
n=0
keyword=input("請輸入您要搜尋的字串:")
for row in htmllist:
    if keyword in row: 
        n+=1
print(f"{keyword} 字串在網頁中找到{n}筆!")
