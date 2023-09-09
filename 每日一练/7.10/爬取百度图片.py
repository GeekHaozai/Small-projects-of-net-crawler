import re
import time

import requests
i = 1
def get_pic(selection,keyword,page_num):
    match selection:
        case "百度":
            headers = {
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51",
                "Cookie":"BDqhfp=%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87%26%260-10-1undefined%26%263672%26%263; BDUSS=WxRQXhuTE8zRGlkRWNIc2ZTNXZHT344TFhMTDF5akhWTGIzMEh6eU9uOHE0MHRrRVFBQUFBJCQAAAAAAQAAAAEAAACJnPYFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACpWJGQqViRkQ; BDUSS_BFESS=WxRQXhuTE8zRGlkRWNIc2ZTNXZHT344TFhMTDF5akhWTGIzMEh6eU9uOHE0MHRrRVFBQUFBJCQAAAAAAQAAAAEAAACJnPYFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACpWJGQqViRkQ; newlogin=1; BAIDUID=DD54F7D1F125ED6630344BAB6C3BB50B:FG=1; BIDUPSID=DD54F7D1F125ED6630344BAB6C3BB50B; PSTM=1681034318; ZFY=7QkotRKrIH:AYl3uWdVWiVkAtHOM3d1L8hp2Is9iam8s:C; BAIDUID_BFESS=DD54F7D1F125ED6630344BAB6C3BB50B:FG=1; H_PS_PSSID=36561_38642_38831_39025_39022_38943_38882_38959_38955_38983_38963_38918_38809_38639_26350_39041; BA_HECTOR=81a50g00800k21a12k8l80a51iandd81o; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; firstShowTip=1; indexPageSugList=%5B%22%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87%22%5D; cleanHistoryStatus=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; userFrom=null; ab_sr=1.0.1_YWU2ZmJmM2MzZGQyYzkxMmJjMDE2N2NiZGE0N2MxOWI0ODRiYjhiYWViNjc4YjcyMWM5ZjljZDJhNWE0NzFlMjZhMDI5MThiYzAxYzFiNmFlMDA0YTEzMGI4ZDQxMzMyZjdiZTI2OThmYjFjZTNjYWU0MDIyNzExZjczNWU3Mzg4OTZjZDIwNDQxMDE2OTdiMWM0MGI3N2EzZDgwMmFmMQ==",
                "Host":"image.baidu.com",
                "Referer":"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111110&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87&oq=%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87&rsp=-1",
            }
            for page in range(1,page_num+1):
                url = f"https://image.baidu.com/search/acjson?tn=resultjson_com&logid=6973045649695582883&ipn=rj&ct=201326592&is=&fp=result&fr=&word={keyword}&cg=girl&queryWord={keyword}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn={page*30}&rn=30&gsm=78&1689001304131="
                print(url)
                ajax_result = requests.get(url,headers=headers).json()
                print(requests.get(url,headers=headers).json())
                pic_urls = ajax_result["data"]
                for item in pic_urls[:-1]:
                    pic_url = item["thumbURL"]
                    print(pic_url)
                    global i
                    with open(f"爬取的百度图片\{i}.jpg","wb") as f:
                        content = requests.get(pic_url)#不知道为什么这里带了请求头反而会403forbidden
                        f.write(content.content)
                        print(f"[INFO]:第{i}张图片保存成功")
                    i = i+1
        case _:
            return "你输了个什么玩意儿，不支持！"

get_pic("百度","美女图片",1000)