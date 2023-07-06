import requests
from bs4 import BeautifulSoup
import xlwt

def get_douban(page):
    url='https://movie.douban.com/top250?start='+str(page*25)+'&filter='
    headers={
        'Cookie': 'bid=snJbVFl8Aqg; __yadk_uid=HPjtIeSLZIOqT2kzRWtZRintj02mJJe4; viewed="35646459"; ll="108288"; __utma=223695111.1005548098.1683288468.1683288468.1685193402.2; __utmz=223695111.1685193402.2.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=DAC0D635C1FBAE61848057777A9FFFB74|8d0893be4ba48dbaa8a1f16851e3a4de; __utma=30149280.1758978808.1683288468.1685193402.1686924468.3; __utmz=30149280.1686924468.3.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=5c731b0714a207b7.1683288466.; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1687057418%2C%22https%3A%2F%2Fwww.bing.com%2F%22%5D; _pk_ses.100001.4cf6=1; ap_v=0,6.0',
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 111.0.0.0Safari / 537.36Edg / 111.0.1661.41'
    }
    try:
        response = requests.get(url,headers=headers)
        print(response.status_code)
        if response.status_code==200:
            html=response.text
            return html
    except Exception:
        return None

def parse_html(html):
    soup=BeautifulSoup(html,'lxml')
    list=soup.find('ol',class_="grid_view").find_all('li')
    for eachfilm in list:
        num=eachfilm.find('em').string
        imgsrc=eachfilm.find('img')['src']
        title=eachfilm.find('span').string
        score=eachfilm.find(class_="star").find(class_="rating_num").string
        quote=eachfilm.find(class_="quote").string
        miaoshu=eachfilm.find('p').text
        print('爬取电影：'+num+'|'+title+'|'+score+'|'+quote)

def save_excel():
    book=xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet=book.add_sheet("豆瓣电影top250",cell_overwrite_ok=True)
    sheet.write(0,0,'名称')
    sheet.write(0, 1, '图片url')
    sheet.write(0, 2, '评分')
    sheet.write(0, 3, '排名')
    sheet.write(0, 4, '作者')
    sheet.write(0,5,'简介')
    book.save('豆瓣Top250部电影.xlsx')

def main():
    for i in range(1,11):
        html=get_douban(i)


