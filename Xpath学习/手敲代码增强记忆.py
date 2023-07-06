from lxml import etree#因为xpath属于lxml库模块

html = """
<html>
<body>
  <iframe src="https://example.com"></iframe>
  <iframe src="https://accounts.douban.com/password/login_popup?login_source=anony"></iframe>
  <iframe src="https://example.com"></iframe>
</body>
</html>
"""


tree=etree.HTML(html)
content=tree.xpath('...')
selected_elements = tree.xpath("//div[@class='container']/*")

#也可以这样
# parser=etree.HTMLParser()
# tree=etree.fromstring(html,parser)
#但是这种方法可以应对更加复杂的请况，如下
# 创建解析器对象并进行自定义配置
# parser = etree.HTMLParser(
#     remove_comments=False,  # 禁止删除注释
#     strip_cdata=False  # 禁止删除CDATA节
# )

