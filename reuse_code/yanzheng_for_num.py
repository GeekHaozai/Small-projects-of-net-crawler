# -*- coding: utf-8 -*-
# @Date    : 2021/10/03
# @Author  : 薄荷你玩
# @Website ：http://www.bhshare.cn

import json
import requests

TOKEN = "977ffdee5"  # token 获取：http://www.bhshare.cn/imgcode/gettoken
URL = 'http://www.bhshare.cn/imgcode/'  # 接口地址


def imgcode_online(imgurl):
    """
    在线图片识别
    :param imgurl: 在线图片网址 / 图片base64编码（包含头部信息）
    :return: 识别结果
    """
    data = {
        'token': TOKEN,
        'type': 'online',
        'uri': imgurl
    }
    response = requests.post(URL, data=data)
    print(response.text)
    result = json.loads(response.text)
    if result['code'] == 200:
        print(result['data'])
        return result['data']
    else:
        print(result['msg'])
        return 'error'


def imgcode_local(imgpath):
    """
    本地图片识别
    :param imgpath: 本地图片路径
    :return: 识别结果
    """
    data = {
        'token': TOKEN,
        'type': 'local'
    }

    # binary上传文件
    files = {'file': open(imgpath, 'rb')}

    response = requests.post(URL, files=files, data=data)
    print(response.text)
    result = json.loads(response.text)
    if result['code'] == 200:
        print(result['data'])
        return result['data']
    else:
        print(result['msg'])
        return 'error'


if __name__ == '__main__':
    imgcode_online("https://ts1.cn.mm.bing.net/th/id/R-C.723529c36468eba36932ec13166f41c2?rik=IK9mOrqKhx5QNg&riu=http%3a%2f%2fwww.zhayoujizhijia.com%2ffile%2fupload%2f201910%2f26%2f10011326364.jpg&ehk=IVAi0yD9qTaUsG2hjmlmALqkp2e7foeqYIMG0H7VCo0%3d&risl=&pid=ImgRaw&r=0")

    imgcode_local(r"C:\Users\DELL123\Desktop\captcha.png")

    # 输出样例：
    # {'code': 200, 'msg': 'ok', 'data': '74689'}
    # 74689

