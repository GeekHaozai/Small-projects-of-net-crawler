import re
from bs4 import BeautifulSoup
from selenium import webdriver

#因为不知道怎么抓包，分析抓包找不到什么规律，不如直接selenium可见即可爬

driver = webdriver.Edge()
cookie_str = 'BDUSS_BFESS=WxRQXhuTE8zRGlkRWNIc2ZTNXZHT344TFhMTDF5akhWTGIzMEh6eU9uOHE0MHRrRVFBQUFBJCQAAAAAAQAAAAEAAACJnPYFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACpWJGQqViRkQ; ZFY=7QkotRKrIH:AYl3uWdVWiVkAtHOM3d1L8hp2Is9iam8s:C; BAIDUID_BFESS=DD54F7D1F125ED6630344BAB6C3BB50B:FG=1'

for item in cookie_str.split(';'):
    name_value = item.strip().split('=', 1)
    if len(name_value) < 2:  # 该项没有'='，跳过
        continue
    name, value = name_value
    cookie = {'name': name, 'value': value}
    driver.add_cookie(cookie)

driver.get("https://zhuanlan.zhihu.com/p/389477042")
print(driver.page_source)

#本次以失败告终
#但我不会就此气馁