from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Edge()
driver.get("https://zhuanlan.zhihu.com/p/79682302")
action = ActionChains(driver)
action.move_by_offset(10,10)
action.click()
action.perform()
xm = driver.execute_script("return navigator.userAgent")
print(xm)