import requests

url="http://www.ntnu.edu.tw/"
html=requests.get(url)
html.encoding="utf-8"
print(html.text)