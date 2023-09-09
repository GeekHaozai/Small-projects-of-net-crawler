# 通过执行命令行的形式来启动脚本方便debug
from scrapy.cmdline import execute

execute('scrapy crawl buptspider'.split())
# 参数是列表而不是字符串


# 或者是：（调用框架API）
# from scrapynb.spiders.buptspider import BuptspiderSpider
# from scrapy.crawler import CrawlerProcess
#
# process=CrawlerProcess()
# process.crawl(BuptspiderSpider)
# process.start()
