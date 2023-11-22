import requests,os
from bs4 import BeautifulSoup

url="https://www.edu.tw/"
html=requests.get(url+"Default.aspx")
bs=BeautifulSoup(html.text,"html.parser")
pics_dir="pics"
if not os.path.exists(pics_dir):
    os.mkdir(pics_dir) 
imgs=bs.find_all("img") 
for img in imgs:
    src=img.get("src") 
    if src!=None and (".jpg" in src or ".png" in src):
        file_n=src.split("/")[-1] 
        if src.startswith("http"):
            full_path=src    
        else:
            full_path=url+src        
        try: 
            image=requests.get(full_path)
            f=open(os.path.join(pics_dir,file_n),"wb")
            f.write(image.content)
            print(f"下載成功：{file_n}")
            f.close()
        except: 
            print(f"無法下載：{file_n}")
