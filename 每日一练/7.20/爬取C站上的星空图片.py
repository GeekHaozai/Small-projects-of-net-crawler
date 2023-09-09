import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import requests

i = 101
driver = webdriver.Edge()
wait = WebDriverWait(driver, 10)
driver.maximize_window()
driver.get('https://civitai.com/images?tags=1468&view=feed')
# time.sleep(200)
# coo=driver.get_cookies()
# print(coo)
while True:
    pic = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="freezeBlock"]/div/div[1]/div/div/img')))
    try:
        pic_url = pic.get_attribute('src')
    except:
        print("这里的src属性没搞到")
        continue
    button_next = driver.find_element(By.XPATH,'//*[@id="freezeBlock"]/div/div[1]/button[2]')
    with open(fr'C:\Users\DELL123\Desktop\study\爬虫项目\每日一练\7.20\爬取的C站图片\{i}.jpeg',"wb") as f:
        r = requests.get(pic_url)
        f.write(r.content)
    print(f"[INFO]:第{i}张保存成功",pic_url)
    print("当前url是:",driver.current_url)
    i += 1
    if i%100==0:
        shuru = None
        while shuru != 'y':
            shuru = input("该换页了，输入'y'确认")
    button_next.click()

driver.find_element(By)
#到这就不知道怎么进行下去了，只能继续深入学习扩展知识面