import ddddocr

ocr = ddddocr.DdddOcr()

with open(r"C:\Users\DELL123\Desktop\captcha.png", 'rb') as f:
    img_bytes = f.read()

res = ocr.classification(img_bytes)

print(res)