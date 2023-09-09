from pytesseract import pytesseract
from PIL import Image
text = pytesseract.image_to_string(Image.open(r"C:\Users\DELL123\Desktop\下载.png"))
img = Image.open(r"C:\Users\DELL123\Desktop\R-C.png")
#也可以使用byte流导入图片
#img = Image.open(io.BytesIO(n))

#转为灰度图
img = img.convert("L")
#保存

#接下来进行二值化,阈值分割法，，threshold为分割点(我也不懂是啥，先无脑套用吧~)
threshold = 140
Table = []
for j in range(256):
    if j < threshold:
        Table.append(0)
    else:
        Table.append(1)
out = img.point(Table,"1")

#识别
text = pytesseract.image_to_string(out)
print(text)