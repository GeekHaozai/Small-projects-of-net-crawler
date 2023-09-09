import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains  # 用于拖动
from selenium.webdriver.common.alert import Alert

# 实例一个driver
driver = webdriver.Edge()
driver.get('http://www.baidu.com')

# 查找单个元素
driver.find_element(By.ID, 'my-element-id')
# driver.find_element_by_id('my-element-id')似乎已经废弃？
driver.find_element(By.CSS_SELECTOR, '...')
driver.find_element(By.NAME, '...')
driver.find_element(By.XPATH, '...')
driver.find_element(By.TAG_NAME, '...')
driver.find_element(By.CLASS_NAME, '...')
driver.find_element(By.LINK_TEXT, '...')

# 查找多个元素
driver.find_elements(By.ID, 'my-element-id')
# driver.find_elements_by_id('my-element-id')似乎已经废弃？
elements1 = driver.find_elements(By.CSS_SELECTOR, ".container")
elements2 = driver.find_elements(By.NAME, "username")
elements3 = driver.find_elements(By.XPATH, "//div[contains(text(), 'Hello')]")
elements4 = driver.find_elements(By.TAG_NAME, "a")
elements5 = driver.find_elements(By.CLASS_NAME, "highlighted")
elements6 = driver.find_elements(By.LINK_TEXT, "Learn More")  # "Learn More"为链接文本

# 元素的交互
input = driver.find_element(By.NAME, '...')
input.send_keys('whnb')
input.clear()
button = driver.find_element(By.CLASS_NAME, '...')
button.click()

# 鼠标操作
# 切换到目标元素所在的frame
driver.switch_to.frame('iframeResult')
# 确定拖拽目标的起点和终点
source = driver.find_element(By.ID, '...')
target = driver.find_element(By.ID, '...')
# 形成动作链
action = ActionChains(driver)
action.drag_and_drop(source, target)
action.perform()

# 执行js脚本
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
driver.execute_script("alert('弹出警告')")

# 获取元素信息
logo = driver.find_element(By.ID, '...')
print(logo)
# 请注意，为了避免与关键字冲突，通常在编程中建议避免使用关键字作为变量名或属性名。
print(logo.get_attribute('class'))  # class是关键字所以不能直接.class
print(logo.text)  # 获取元素的文本内容
print(logo.id)
print(logo.location)  # 获取元素在页面上的位置，返回的是一个字典，包含x和y坐标值。
print(logo.tag_name)  # 获取元素的标签名称，如"div"、"a"等。
print(logo.size)  # 获取元素的大小，返回的是一个字典，包含宽度和高度值。

# 等待，适用于元素不会立即出现的情况

# 隐式等待
driver.implicitly_wait(10)
# ...然后继续操作

# 显式等待
# 引入两个文件
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)  # 设置等待时间
input = wait.until(EC.presence_of_element_located((By.ID, "q")))  # 等待元素出现
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))  # 等待元素可点击
print(input, button)

# 浏览器的前进与后退
driver.back()
time.sleep(1)
driver.forward()

# cookie的处理
driver.get_cookies()  # 获取页面上所有cookie
print(driver.get_cookies())
driver.add_cookie({
    'name': 'name',
    'domain': 'www.zhihu.com',
    'value': 'germey'
})  # 添加cookie
driver.delete_all_cookies()  # 删除所有cookies

# 页面的切换
driver.execute_script('window.open()')  # 脚本打开另外一个页面
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])
driver.get('http://www.python.org')

# 定位iframe
driver.switch_to.frame('authframe')  # 通过‘id'或者name属性查找并且转到
driver.switch_to.default_content()  # 切换回主文档，因为切换到iframe后无法对主文档进行操控
# 如果没有name或者id，
# 使用xpath
driver.switch_to.frame(driver.find_element(By.XPATH, '...'))
# 使用其他属性如src
driver.switch_to.frame(By.XPATH,
                       "//iframe[contains(@src,'//acounts.douban.com/password/login_popup?login_source=anony')]")
driver.switch_to.frame(By.XPATH, "//*[@id='anony-ref-new']/div/div[0]/iframe")

driver.close()

