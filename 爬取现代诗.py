import requests
import re
import json

# url='http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1'
# html=requests.get(url).text
# print(html)
# #pattern=re.compile('<li>.*?list_num.*?(\d+).*?<image src="(.*?)".*?class="name".*?title="(.*?)".*?class="star".*?class="tuijian">(.*?)<.*?class="publisher_info.*?target="_blank">(.*?)<.*?class="biaosheng".*?<span>(.*?)<.*?class="price".*?<p><span class="price_n">&yen;(.*?)</span>.*?</li>',re.S)
# pattern=re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?',re.S)
# items=re.findall(pattern,html)
# print(items)
# html='''<li>
#     <div class="list_num red">1.</div>
#     <div class="pic"><a href="http://product.dangdang.com/29330332.html" target="_blank"><img src="http://img3m2.ddimg.cn/97/25/29330332-1_l_27.jpg" alt="从零开始学基金"  title="从零开始学基金"/></a></div>
#     <div class="name"><a href="http://product.dangdang.com/29330332.html" target="_blank" title="从零开始学基金">从零开始学基金</a></div>
#     <div class="star"><span class="level"><span style="width: 100%;"></span></span><a href="http://product.dangdang.com/29330332.html?point=comment_point" target="_blank">15081条评论</a><span class="tuijian">100%推荐</span></div>
#     <div class="publisher_info"><a href="http://search.dangdang.com/?key=黄士铨" title="黄士铨" target="_blank">黄士铨</a></div>
#     <div class="publisher_info"><span>2021-11-01</span>&nbsp;<a href="http://search.dangdang.com/?key=电子工业出版社" target="_blank">电子工业出版社</a></div>
#             <div class="biaosheng">五星评分：<span>8043次</span></div>
#     <div class="price">
#         <p><span class="price_n">&yen;37.50</span>
#                         <span class="price_r">&yen;75.00</span>(<span class="price_s">5.0折</span>)
#                     </p>
#                     <p class="price_e">电子书：<span class="price_n">&yen;30.00</span></p>
#                 <div class="buy_button">
#                           <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29330332');" class="listbtn_buy">加入购物车</a>
#
#                         <a name="" href="http://product.dangdang.com/1901313238.html" class="listbtn_buydz" target="_blank">购买电子书</a>
#                         <a ddname="加入收藏" id="addto_favorlist_29330332" name="" href="javascript:showMsgBox('addto_favorlist_29330332',encodeURIComponent('29330332&platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
#     </div>
#     </div>
#     </li>'''
# pattern2 = re.compile('<li>.*?list_num.*?(\d+).*?<img src="(.*?)".*?class="name".*?title="(.*?)".*?class="star".*?class="tuijian">(.*?)<.*?class="publisher_info.*?target="_blank">(.*?)<.*?class="biaosheng".*?<span>(\d+).*?class="price".*?<p><span class="price_n">&yen;(.*?)</span>.*?</li>', re.S)
# pattern1 = re.compile('<li>.*?list_num.*?(\d+).*?<img src="(.*?)".*?class="name".*?title="(.*?)".*?class="star".*?class="tuijian">(.*?)<.*?class="publisher_info.*?target="_blank">(.*?)<.*?class="biaosheng".*?<span>(.*?)<.*?class="price".*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',re.S)
# items=re.findall(pattern1,html)
# print(items)
item={'range': '441', 'iamge': 'http://img3m4.ddimg.cn/43/27/29559364-1_l_1.jpg', 'title': '炙热的你：关于了不起的女性更年期的一切', 'recommend': '100%推荐', 'author': '希拉', 'times': '18次', 'price': '49.00'}
chuli=json.dumps(item, ensure_ascii=False) + '\n'
print((chuli))