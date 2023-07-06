import time

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Edge()
browser.get("https://accounts.douban.com/passport/login_popup?login_source=anony")  # 这里替换成您要访问的页面URL

# 使用显式等待等待目标元素加载
wait = WebDriverWait(browser, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/ul[1]/li[2]')))#这个等待很重要，不然会报错说没找到
button.click()

time.sleep(10)
browser.quit()
