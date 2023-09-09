import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Edge()
driver.get("https://www.bilibili.com/")

wait = WebDriverWait(driver, 10)
input = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#nav-searchform > div.nav-search-content > input')))
# submit = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"nav-searchform\"]/div[2]")))

input.send_keys("坤坤")
# submit.click()
input.send_keys(Keys.ENTER)

print('[INFO]:A NEW WINDOW HAS BEEN OPENED.')
driver.switch_to.window(driver.window_handles[1])

time.sleep(10)
