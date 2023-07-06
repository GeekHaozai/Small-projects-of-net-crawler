import requests

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41'

}
response=requests.get('https://zhuanlan.zhihu.com/p/389477042',headers=headers)
response.encoding='utf-8'
print(response.text)