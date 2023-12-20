# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver=webdriver.Chrome() 
# driver.get("https://www.google.com.tw")
# q=driver.find_element_by_name("q")
# q.send_keys("銘傳大學")
# q.send_keys(Keys.RETURN)
# m=driver.find_element_by_partial_link_text("亞洲第一所").click()
# driver.close()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("https://www.google.com.tw")
q=driver.find_element(By.NAME,"q")
q.send_keys("銘傳大學")
q.send_keys(Keys.RETURN)
m=driver.find_element(By.PARTIAL_LINK_TEXT,"亞洲第一所").click()
driver.close()