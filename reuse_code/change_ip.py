import requests
def get_ip():
    url = "http://www.857ip.cn/"
    ip = requests.get("http://v2.api.juliangip.com/dynamic/getips?num=1&pt=1&result_type=json&trade_no=1372767291920383&sign=15dce8f258eb9230f1e777f61c2b2521") #这里是你生成的API链接
    print(ip.json())
    ip_text = ip.json()["data"]["proxy_list"][0]
    return ip_text

# import requests
# proxies = {
#     'http': 'http://'+ip_text,
#     'https': 'http://'+ip_text,
# }
#
# response = requests.get('http://www.baidu.com', proxies=proxies)
#
# print(response.text)