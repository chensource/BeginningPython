import scrapy
import math


class AnjukeScrapy(scrapy.Spider):
    name = 'anjukeinfo'
    xiaoqu_list_url = "https://wuhan.anjuke.com/community/"
    district_list = [
        # 东湖高新，洪山，江岸，
        # 东西湖，汉阳，武昌，江汉，经济开发，硚口，黄陂，江夏，青山，蔡甸，新洲，汉南，其他
        'wuchanga',
        'hongshana',
        'jiangan',
        'hanyang',
        'jianghana',
        'qiaokou',
        'dongxihu',
        'jiangxiat',
        'huangpiz',
        'qingshan',
        'caidianz',
        'xinzhouz',
        'hannanz'
        #'qita1'  应业务线要求，去掉非武汉市城区的楼盘
    ]

    def start_requests(self):
        for district in self.district_list:
            url = self.xiaoqu_list_url + district + "/p1/?from=navigation'"
            yield scrapy.Request(url=url, callback=self.parse_xiaoqu_list)

        # url = "https://wuhan.anjuke.com/community/?from=navigation"
        # yield scrapy.Request(url=url, callback=self.parse_xiaoqu_list)

    def parse_xiaoqu_list(self, response):
        for box in response.xpath('//div[@class="li-info"]'):
            url = box.xpath('./h3//a/@href').extract()[0]
            name = box.xpath('./h3//a/@title').extract()[0]
            area = box.xpath(
                './/address/text()').extract()[0].split('-')[0].strip().replace('［', '')

            region = box.xpath(
                './/address/text()').extract()[0].split('-')[1].strip().split('］')[0]

            pid = str(url).replace(
                'https://wuhan.anjuke.com/community/view/', '').replace('/', '')

            yield {
                "pid": pid, "name": name, "area": area, 'region': region,  "url": url}

        for page in response.xpath('//div[@class="multi-page"]'):
            page_links = page.xpath('.//a[@class="aNxt"]/@href').extract()[0]
            yield scrapy.Request(url=page_links, callback=self.parse_xiaoqu_list)
