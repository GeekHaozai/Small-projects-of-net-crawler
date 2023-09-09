from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import selenium
import cv2
import requests



password = '''
这里输入输入QQ密码
'''

def get_pos(image):
    blurred = cv2.GaussianBlur(image, (5, 5), 0,0)
    # Canny
    # edges = cv2.Canny(image, threshold1,threshold2, apertureSize, L2gradient)
    # threshold1计算过程中使用的第一个阈值，通常为最小阈值
    # threshold2计算过程中使用的第二个阈值，通常为最大阈值
    # apertureSize 可选参数，Sobel算子的孔径大小
    # L2gradient 可选参数，计算图像梯度的标识，默认值为False，值为True时会采用更精确的方法计算。
    canny = cv2.Canny(blurred, 200, 400)
    # contours, hierarch = cv2.findCours(image, mode, methode)
    # cv2.RETR_EXTERNAL只检测外轮廓
    # cv2.CHAIN_APPROX_SIMPLE只保存水平，垂直或对角线轮廓的端点
    # contours 检测出所有的轮廓，列表类型，每一个元素都是某个轮廓的像素坐标数组
    # hierarchy 轮廓之间的层次关系
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # print(contours, hierarchy)
    for i, contour in enumerate(contours):
        M = cv2.moments(contour)
        if M['m00'] == 0:
            cx = cy = 0
        else:
            cx, cy = M['m10'] / M['m00'], M['m01'] / M['m00']
        if 6000 < cv2.contourArea(contour) < 8000 and 370 < cv2.arcLength(contour, True) < 390:
            if cx < 400:
                continue
            print(cv2.contourArea(contour))
            print(cv2.arcLength(contour, True))
            x, y, w, h = cv2.boundingRect(contour)  # 外接矩形
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # cv2.imshow('image', image)
            # cv2.imwrite('111.jpg', image)
            return x
    return 0

url = 'https://mail.qq.com'
wb = webdriver.Chrome()
# 设置超时停止加载
wb.set_page_load_timeout(4)
try:
    wb.get(url)
# 当超过指定时间以后，页面会停止加载并报错，使用except会接收错误，pass跳过当前错误
except selenium.common.exceptions.TimeoutException:
    pass

wb.implicitly_wait(10)
wb.switch_to.frame("login_frame")

wb.find_element_by_xpath('//*[@id="u"]').send_keys('这里输入QQ邮箱')
wb.find_element_by_xpath('//*[@id="p"]').send_keys(password)

wb.find_element_by_xpath('//*[@id="p_low_login_enable"]').click()
wb.find_element_by_xpath('//*[@id="login_button"]').click()
# wb.switch_to.default_content()
wb.switch_to.frame("tcaptcha_iframe")

# 保存验证码
verify_img = wb.find_element_by_xpath('//*[@id="slideBg"]')
img_url = verify_img.get_attribute('src')
print(img_url)
content = requests.get(img_url).content
with open('verift_img.jpg', 'wb') as f:
    f.write(content)
# 会把页面的其它元素也截取下来，不适用
# verify_img = wb.find_element_by_xpath('//*[@id="slideBg"]').screenshot_as_png
verify_img = cv2.imread('verift_img.jpg')
x = get_pos(verify_img)
print(x)
#
result = int(x * 0.41) - 30
slide = wb.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
ActionChains(wb).drag_and_drop_by_offset(slide, result, 0).perform()

wb.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]').click()
# 如果验证码没有识别正确，判断，之后重新识别，直到通过验证
try:
    wb.switch_to.frame("verify")
    wb.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[1]').click()
except selenium.common.exceptions.NoSuchWindowException:
    print('将验证码识别的函数打包在里面重新识别')
    print('1111111111')
# 继续后面的操作
cv2.waitKey(0)
cv2.destroyAllWindows()
