import scrapy
from bs4 import BeautifulSoup
from spiders.items import SpidersItem



class MovieSpider(scrapy.Spider):
    # 定义爬虫名称
    name = 'douban'
    allowed_domains = ['maoyan.com']
    # 起始URL列表
    start_urls = ['https://maoyan.com/films?showType=3']

#   注释默认的parse函数
#   def parse(self, response):
#        pass


    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        url = f'https://maoyan.com/films?showType='
        yield scrapy.Request(url=url, callback=self.parse)
            # url 请求访问的网址
            # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')
        link = movies.response.xpath('./a/@href')
        for i in link:
            i1 = Selector(response=response).xpatn('//div[class="movie-brief-container"]')
            # 在items.py定义
            item = SpidersItem()
            title = movie.xpath('./div[1]/text()').get()
            ca = movie.xpath('./div[3]/text()').get().extract()
            date  = movie.xpath('./div[4]/text()').get()
            yield  item

    # 解析具体页面
   """  def parse2(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('div', attrs={'class': 'related-info'}).get_text().strip()
        item['content'] = content
        yield item """