from bs4 import BeautifulSoup

html_text="""
<html><head><title>國立臺灣大學系統</title></head>
<body>
<p class="title"><b>三校聯盟 NTU SYSTEM</b></p>
<p class="ntu_system">
<a href="http://www.ntu.edu.tw" class="union" id="link1">臺灣大學</a>
<a href="http://www.ntnu.edu.tw" class="union" id="link2">臺灣師範大學</a>
<a href="http://www.ntust.edu.tw" class="union" id="link3">臺灣科技大學</a>
</p></body></html>
"""
bs=BeautifulSoup(html_text,"html.parser") 
print("1：",bs.title) #網頁標題屬性
print("2：",bs.find("a")) #<a>標籤
print("3：",bs.find("b")) #<b>標籤
print("4：",bs.find_all("a",{"class":"union"})) #印出<a>標籤且class為union
print("5：",bs.find("a",{"id":"link2"})) #印出<a>標籤且id為link2
print("6：",bs.find("a",{"href":"http://www.ntust.edu.tw"}))
web=bs.find("a", {"id":"link1"}) 
print("7：",web.get("href")) #使用get取出網址
data=bs.select(".union") #select會傳回串列
print("8：",data[0].text) #串列的第一項
print("9：",data[1].text) 
print("10：",bs.select("#link3"))