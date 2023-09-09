from selenium import webdriver
from time import sleep

try:
    browser = webdriver.Edge()
    browser.get('https://webvpn.bupt.edu.cn/login')

except:
    print('出了点错误')
