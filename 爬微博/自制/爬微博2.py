import requests
import re
from bs4 import BeautifulSoup
import datetime
from datetime import timedelta

start = datetime.datetime(2022, 12, 31, 20, 0, 0)
end = datetime.datetime(2023, 6, 30, 20, 0, 0)



with open("./数据2.csv", "w", encoding="utf-8", newline="") as f:
    f.write("用户名称，发布时间，发布内容，内容中的转发内容")
def get_each_page(page,time):
    headers = {
        "Cookie": "SINAGLOBAL=997143862574.7164.1692108642728; _s_tentry=-; Apache=5240139554815.309.1692167707318; ULV=1692167707343:3:3:3:5240139554815.309.1692167707318:1692164279293; SCF=AjN22hi_dtJ0aCVJcz_IsxKUfMBU3oXZzTbf_kAhYqdhrGFl9btZigh81LgCN01mbpgYTupuTDsu0tKrqrvau20.; SUB=_2A25J2B50DeRhGeFG7VAY8CnKyz-IHXVqrAi8rDV8PUJbmtANLUT3kW9NeTDsUoVS5aKb_dDCZ0jd97N0Bj6QmyAp; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWV2c6xW-_YQnQaD2NvJcqk5JpX5K-hUgL.FoMRSoz4ehMcehe2dJLoI79hIGiad.nt; ALF=1694759712; SSOLoginState=1692167716",

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51"
    }
    params = {
        "q": "系",
        "typeall": "1",
        "suball": "1",
        "timescope": time,
        "Refer": "g",
        "page": page
    }
    r = requests.get("https://s.weibo.com/weibo",headers=headers,params=params)
    r.encoding = "utf-8"
    pattern1 = re.compile("<!--微博内容-->(.*?)<!--/微博内容-->",re.DOTALL)
    print(r.text)
    contents = pattern1.findall(r.text)
    for content in contents:
        print("===================================================")
        soup = BeautifulSoup(content,"lxml")
        name = soup.div.p["nick-name"]
        print("昵称：",name)
        text = soup.div.p.text.strip()
        print("内容：",text)

        time_content = re.findall('<div class="from" >(.*?)</div>', content, re.DOTALL)
        soup_time = BeautifulSoup(time_content[0], "lxml")
        time = soup_time.a.text.strip()
        print("发布时间：", time)
        if "2022" not in time and "月" not in time:
            continue
        zhuanfa_content = ""
        zhuanfa = re.findall("<!--转发微博-->(.*?)<!--/转发微博-->",content,re.DOTALL)
        if zhuanfa:
            zhuanfa_soup = BeautifulSoup(zhuanfa[0],"lxml")
            zhuanfa_content = zhuanfa_soup.div.div.div.div.p.text.strip()
            print("转发内容：",zhuanfa_content)
        with open("./数据2.csv","a",encoding="utf-8") as f:
            f.write("\n")
            f.write(",".join([name,time,text,zhuanfa_content]))

while start <= end:
    end_hour = start + timedelta(hours=1)
    if start.hour == 20:
        start_time = start.strftime("%Y-%m-%d-%H")
        end_time = end_hour.strftime("%Y-%m-%d-%H")
        time = f"custom:{start_time}:{end_time}"
        for page in range(1, 51):
            get_each_page(page,time)
    start = end_hour



