import scrapy
from ..items import ScrapynbItem


class BuptspiderSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    # 重写这个方法来自定义对爬虫起始页面的爬取设置，如设置cookies等
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        detail_pages = response.xpath('//div[@class="hd"]/a/@href').extract()
        titles = response.xpath('//ol[@class="grid_view"]//div[@class="hd"]/a/span[1]/text()').extract()
        brief_comments = response.xpath('//p[@class="quote"]/span/text()').extract()
        for index in range(len(titles)):
            detail_page = detail_pages[index]
            title = titles[index]
            brief_comment = brief_comments[index]
            yield scrapy.Request(detail_page, callback=self.parse_details, meta={
                "title": title,
                "brief_comment": brief_comment,
            })

        # for detail_page in detail_pages:
        #     yield scrapy.Request(detail_page, callback=self.parse_details)
        # for title in titles:
        #     print(title)
        next_page = response.xpath('//span[@class="next"]/a/@href').extract_first()
        base_url = 'https://movie.douban.com/top250'
        if next_page:
            yield scrapy.Request(url=base_url + next_page, callback=self.parse)

    def parse_details(self, response):
        meta = response.meta
        contents = response.xpath('//*[@id="link-report"]//text()').extract()
        contents = [content.strip() for content in contents]
        content = "".join(contents)
        print(meta['title'])
        print(meta['brief_comment'])
        print(content)
        item = ScrapynbItem()
        item['title'] = meta['title']
        item['brief_comment'] = meta['brief_comment']
        yield item
