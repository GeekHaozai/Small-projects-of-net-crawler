import requests

page = 120
headers = {
    "Sec-Ch-Ua-Platform":"Android",
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.51",
    "X-Requested-With":"XMLHttpRequest",
    "X-Xsrf-Token":"5f5780",
    "Referer":"https://m.weibo.cn/search?containerid=100103type%3D1%26q%3D%E7%B3%BB"
}
params = {
    "containerid": "100103type=1&q=系",
    "page_type": "searchall",
    "page":page,
}
url = "https://m.weibo.cn/api/container/getIndex"
r = requests.get(url,params=params,headers=headers)
r.encoding = "UTF-8"
print(r.json())
res = r.json()
cards = res["data"]["cards"]
for card in cards:
    name = card["card_group"][0]["mblog"]["user"]["screen_name"]
    text = card["card_group"][0]["mblog"]["text"]
    time = card["card_group"][0]["mblog"]["created_at"]
    print([name,text,time])


