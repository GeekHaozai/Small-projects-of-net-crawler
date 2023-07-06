from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

driver=webdriver.Edge()
driver.get('http://www.baidu.com')
input=driver.find_element(By.ID,'kw')
input.send_keys('火影忍者')
input.send_keys(Keys.ENTER)
#这里不需要找按钮了，反正输入框回车直接就能搜索
#button=driver.find_element(By.)
wait=WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.ID,'content_left')))
print(driver.current_url)
print(driver.page_source)
print(driver.get_cookies())
