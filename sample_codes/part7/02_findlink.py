# from selenium import webdriver

# driver=webdriver.Chrome() 
# driver.get("https://www.google.com.tw")
# e=driver.find_element_by_link_text("Gmail")
# e.click()
# driver.close()

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.google.com.tw")
e=driver.find_element(By.LINK_TEXT,"Gmail")
e.click()
driver.close()