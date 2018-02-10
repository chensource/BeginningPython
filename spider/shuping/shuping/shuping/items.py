import scrapy


class YswItem(scrapy.Item):
    # 发帖时间
    time = scrapy.Field()
    # 获得赞同数量
    agree = scrapy.Field()
    # 二级评论数量
    sec_num = scrapy.Field()
    # 一级评论内容
    fir_text = scrapy.Field()


class YswItems(scrapy.Item):
    # 发帖时间
    time = scrapy.Field()
    # 获得赞同数量
    agree = scrapy.Field()
    # 二级评论数量
    sec_num = scrapy.Field()
    # 一级评论内容
    fir_text = scrapy.Field()
    # 二级评论内容
    sec_text = scrapy.Field()
