from selenium import webdriver
import requests

driver = webdriver.Edge()
driver.get("https://www.bilibili.com/")

print(driver.page_source)

