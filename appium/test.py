import time

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
server = "http://localhost:4723/wd/hub"
desired_caps = {
  "platformName": "Android",
  "appium:deviceName": "SM_N976N",
  "appium:appPackage": "com.tencent.mm",
  "appium:appActivity": "com.tencent.mm.ui.LauncherUI"
}
driver = webdriver.Remote(server,desired_caps)
wait = WebDriverWait(driver,20)
time.sleep(10)
el1 = driver.find_element(by=AppiumBy.ID, value="com.tencent.mm:id/j_9")
el1.click()
el2 = driver.find_element(by=AppiumBy.ID, value="com.tencent.mm:id/cd7")
el2.send_keys("15197745378")
