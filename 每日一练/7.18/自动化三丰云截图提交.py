import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options


driver = webdriver.Edge()
driver.get("https://www.sanfengyun.com/login/")
driver.maximize_window()

zh_input = driver.find_element(By.ID,"userName")
zh_input.send_keys(15197745378)
mm_input = driver.find_element(By.ID,"passwordInput")
mm_input.send_keys("WenHao0425")
login_button = driver.find_element(By.ID,"loginSubmit")
login_button.click()

control = driver.find_element(By.XPATH,"//*[@id=\"header\"]/div/div/div[1]/div/div[2]/ul/li[2]/a")
control.click()

product_page_button = driver.find_element(By.XPATH,"//*[@id=\"app\"]/div[2]/div[1]/ul/li[3]")
product_page_button.click()

free_fwq_page = driver.find_element(By.XPATH,"//*[@id=\"app\"]/div[2]/div[2]/div[1]/dl[1]/dd/div[2]")
free_fwq_page.click()

wait = WebDriverWait(driver,10)
free_continue = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"app\"]/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/div[6]/div[3]/div/button/span")))
free_continue.click()

#接下来打开另一个窗口实现知乎的自动发帖和截图保存
driver.execute_script("window.open()")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://zhuanlan.zhihu.com/")
driver.implicitly_wait(10)
driver.delete_all_cookies()
cookies = [{'domain': 'zhuanlan.zhihu.com', 'httpOnly': False, 'name': 'osd', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'U1AdAk5VnCDJdso6Q1VRfn6XjC1dHc9ZgiCxQAcZpxSjG5hbenvvm617wzNOnAElDaCgeGhbu85e7GqsKZzniV0='}, {'domain': 'zhuanlan.zhihu.com', 'httpOnly': False, 'name': 'JOID', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'W1AXAU9dnCrKd8I6SVZQdn6djyxVHcVagyixSgQYrxSpGJlTenHsmqV7yTBPlAEvDqGoeGJYusZe5mmtIZztilw='}, {'domain': 'zhuanlan.zhihu.com', 'httpOnly': False, 'name': 'SESSIONID', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'eQcCgSDYmBaWxa0bvvaY26WKznQKTBB2E8HYBuwFHR6'}, {'domain': '.zhuanlan.zhihu.com', 'httpOnly': False, 'name': 'Hm_lpvt_bff3d83079cef1ed8fc5e3f4579ec3b3', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1689680425'}, {'domain': '.zhuanlan.zhihu.com', 'expiry': 1721216424, 'httpOnly': False, 'name': 'Hm_lvt_bff3d83079cef1ed8fc5e3f4579ec3b3', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1689680425'}, {'domain': '.zhihu.com', 'httpOnly': True, 'name': 'o_act', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'login'}, {'domain': '.zhihu.com', 'httpOnly': True, 'name': 'expire_in', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '15552000'}, {'domain': '.zhihu.com', 'httpOnly': False, 'name': 'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1689680424'}, {'domain': 'zhuanlan.zhihu.com', 'httpOnly': False, 'name': 'KLBRSID', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '81978cf28cf03c58e07f705c156aa833|1689680423|1689680412'}, {'domain': '.zhihu.com', 'expiry': 1705232423, 'httpOnly': True, 'name': 'z_c0', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '2|1:0|10:1689680422|4:z_c0|92:Mi4xU0x4S0xRQUFBQUFBQUZvVjdFWWFGeGNBQUFCZ0FsVk5Kc2lqWlFBR0lWX29rT1V1VkdzYmdiYWVhMkhpVXkxVzhB|e8b5040e9e78726db321444505ea029a109c8e907ff3f797779d4dab8ec58f56'}, {'domain': '.zhihu.com', 'expiry': 1692272415, 'httpOnly': True, 'name': 'captcha_session_v2', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '2|1:0|10:1689680414|18:captcha_session_v2|88:bEN3ck16eFZVZEhDQ1JneEUzMGRqbW5yek5nNnU0STU4dkRxVnpZY3pwenB6b1RMS3l5ZnNEQm5jWUY4bkZ1aQ==|ee63db681850d9714a5c07bcf0f0ffcecf6c65f2d1121728e1276746dd8b50ce'}, {'domain': '.zhihu.com', 'httpOnly': True, 'name': 'ref_source', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'zhuanlan'}, {'domain': '.zhihu.com', 'expiry': 1721216424, 'httpOnly': False, 'name': 'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1689680414'}, {'domain': '.zhihu.com', 'expiry': 1724240414, 'httpOnly': False, 'name': 'd_c0', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'AABaFexGGhePTv_iVkvdIOG6HDSxh5m-ZjU=|1689680413'}, {'domain': '.zhihu.com', 'httpOnly': False, 'name': '_xsrf', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '846550f6-3d34-4e8e-9c5e-3648f5183298'}, {'domain': '.zhihu.com', 'expiry': 1724240413, 'httpOnly': False, 'name': '_zap', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '91846f02-7191-435e-8d5a-4fd9a68e0851'}]
for cookie in cookies:
    if 'expiry' in cookie:
        del cookie['expiry']
    driver.add_cookie(cookie)
driver.refresh()
driver.get("https://zhuanlan.zhihu.com/write")

title = '三丰云：释放你的创造力，全新免费虚拟主机与云服务器等你来体验'
text = '''您是否想要拥有一台可以满足您业务需求，功能强大且成本低廉的服务器？是的，现在就有这样的机会！让我来为您介绍三丰云（访问链接）的免费虚拟主机和免费云服务器。

三丰云是一家提供全面的云服务解决方案的公司，他们最新的免费虚拟主机和免费云服务器服务将极大地提高你的工作效率。与传统的服务器不同，三丰云的服务器提供了强大的计算能力，同时又保证了数据的安全性和私密性。

经过我们的深度体验，三丰云的免费虚拟主机和免费云服务器性能出色，稳定性良好。这不仅为我们的业务流程提供了强大的支持，也节约了我们大量的IT硬件投资。在使用的过程中，我们还能感受到三丰云对于用户体验的重视，他们的专业团队始终在我们需要的时候提供支持和帮助。

总的来说，三丰云的免费虚拟主机和免费云服务器不仅功能强大，而且高效稳定，性价比极高。无论你是初创企业还是大型公司，三丰云都能为你提供最适合的云服务解决方案。点击这里(https://www.sanfengyun.com/)，立即开始您的云服务之旅吧！'''

title_input = driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/div[2]/div[2]/div[1]/label/textarea')
title_input.send_keys(title)
text_input = driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div/div/div/div')
text_input.send_keys(text)
img_input = driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/div[2]/div[2]/div[2]/div[1]/div/input')
img_input.send_keys(r"C:\Users\DELL123\Desktop\三丰云推广.png")


time.sleep(3)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
submit =driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/div[2]/div[2]/div[2]/div[3]/div[8]/div/button[2]')
time.sleep(3)
submit.click()
time.sleep(50)

url = driver.current_url
current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")  # 格式化时间，将冒号替换为短横线
driver.save_screenshot(fr"C:\Users\DELL123\Desktop\三丰云发帖\{current_time}.png")

driver.switch_to.window(driver.window_handles[0])
url_send = driver.find_element(By.XPATH,'//*[@id="pane-seven"]/form[1]/div/div/div/input')
url_send.send_keys(url)
pic_input = driver.find_element(By.XPATH,'//*[@id="fileImg1"]')
pic_input.send_keys(fr"C:\Users\DELL123\Desktop\三丰云发帖\{current_time}.png")

all_submit = driver.find_element(By.XPATH,'//*[@id="pane-seven"]/form[2]/div/div/button')
all_submit.click()

time.sleep(50000)

time.sleep(20)

# confirm1 = input("请开启代理后输入确认：")
# while confirm1 != 'yes':
#     confirm1 = input("请输入“yes”！")
#继续创建一个窗口进行ai内容自动生成,本来是这样打算的，结果claude生成的内容是固定的，chatgpt进不去，拿不到cookie，于是又只好手动输入了
# driver.execute_script("window.open()")
# driver.switch_to.window(driver.window_handles[2])

# opt = Options()
# opt.add_argument('--proxy-server=http://184.105.182.254:3128')
# driver.get("https://chat.openai.com/?model=gpt-4-mobile")
# time.sleep(300)
# print(driver.get_cookies())
# driver.delete_all_cookies()
# cluade_cookies = [{'domain': '.claude.ai', 'expiry': 1690355754, 'httpOnly': False, 'name': 'intercom-session-lupk8zyo', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'TUcycWhyLzBjMGkraUVBckhadmJ5cHpSNTA5eUwxQitLKzBqYmtTR0hpVmRxM3o1QUFtTHhuSmRNQ1F2SVU3cy0tRFhNR05iNHE2VURqMVpIR01qcFZJUT09--efd36bff21867369a65ed96ab86f9dd8d17f1832'}, {'domain': '.claude.ai', 'expiry': 1713080954, 'httpOnly': False, 'name': 'intercom-device-id-lupk8zyo', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'db3948ff-c53c-498d-82b8-de3e29192cb5'}, {'domain': 'claude.ai', 'expiry': 1692342952, 'httpOnly': True, 'name': 'sessionKey', 'path': '/', 'sameSite': 'Strict', 'secure': True, 'value': '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'}, {'domain': '.claude.ai', 'expiry': 1689752724, 'httpOnly': True, 'name': '__cf_bm', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'JiUG0NpSJVnXQMIvbWRqGSRJ3ig805AVFMHHcCcJ77Y-1689750923-0-AYnoilHBLnRlKyM/ANdFDe14msWP41I5e3jdnuDmzktJxyrQWqnlbZsOaI6FzWf3sCdA43CVmokQ2ZBu2U5SNgM='}]
# for cookie in cluade_cookies:
#     if 'expiry' in cookie:
#         del cookie['expiry']
#     driver.add_cookie(cookie)
# driver.refresh()
# driver.get("https://claude.ai/chats")
#
# cluade_input = driver.find_element(By.XPATH,'/html/body/main/div/div/fieldset/div[1]/div/div/div/p')
# cluade_input.send_keys("请帮我写一篇关于三丰云服务器的推广文的标题，请你只需要回复标题的内容，其它内容不要回复")
# cluade_send = driver.find_element(By.XPATH,'/html/body/main/div/div/fieldset/div[2]/div/button')
# cluade_send.click()
# time.sleep(60)
# biaoti = driver.find_element(By.XPATH,'/html/body/div[5]/div/div[3]/div[4]/div/div[1]/p').text
# print(biaoti)
# cluade_input2 = driver.find_element(By.XPATH,'/html/body/div[5]/div/div[5]/div/fieldset/div[1]/div/div/div')
# cluade_input2.send_keys('请帮我写一篇推广文，要求文章中必须包含“三丰云”"免费虚拟主机"“免费云服务器”字样和大于50字的评测内容，含有三丰云 https://www.sanfengyun.com 链接')
# claude_send2 = driver.find_element(By.XPATH,'/html/body/div[5]/div/div[5]/div/fieldset/div[2]/button')
# claude_send2.click()
# time.sleep(60)
# zhengwen = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[8]/div').text
# print(zhengwen)

# switch_password_login = driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/main/div/div/div/div/div[2]/div/div[1]/div/div[1]/form/div[1]/div[2]")
# switch_password_login.click()
#
# username = driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/main/div/div/div/div/div[2]/div/div[1]/div/div[1]/form/div[2]/div/label/input")
# username.send_keys(15197745378)
#
# password = driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/div/div/div/div[2]/div/div[1]/div/div[1]/form/div[3]/div/label/input')
# password.send_keys("shrodinger8.12")
#
# login_button_zhihu = driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/div/div/div/div[2]/div/div[1]/div/div[1]/form/button')
# login_button_zhihu.click()

