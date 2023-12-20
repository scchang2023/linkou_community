# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup

# driver=webdriver.Chrome() 
# driver.get("https://www.google.com.tw")
# q=driver.find_element_by_name("q")
# q.send_keys("台灣大學")
# q.send_keys(Keys.RETURN)
# bs=BeautifulSoup(driver.page_source,"html.parser")
# links=bs.find_all("h3",{"class":"LC20lb"})
# for link in links:
#     print(link.text)
# driver.close()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

driver=webdriver.Chrome()
driver.get("https://www.google.com.tw")
q=driver.find_element(By.NAME,"q")
q.send_keys("台灣大學")
q.send_keys(Keys.RETURN)
time.sleep(3)
bs=BeautifulSoup(driver.page_source,"html.parser")
links=bs.find_all("h3",{"class":"LC20lb"})
for link in links:
    print(link.text)
# driver.close()