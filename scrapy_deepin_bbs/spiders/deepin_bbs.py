# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy_deepin_bbs.items import ScrapyDeepinBbsItem


class DeepinBbsSpider(CrawlSpider):
    name = 'deepin_bbs'
    allowed_domains = ['bbs.deepin.org']
    start_urls = ['http://bbs.deepin.org/forum.php?mod=guide&view=new&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'view=new&page=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for article in response.css('.bm_c > table:nth-child(2) tbody'):
            i = ScrapyDeepinBbsItem()
            #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
            #i['name'] = response.xpath('//div[@id="name"]').extract()
            #i['description'] = response.xpath('//div[@id="description"]').extract()

            i['title'] = article.css('td.common a.xst::text').extract()[0]
            # i['forum_plate'] = article.css
            # i['autor_name'] = article.css
            # i['post_date'] = article.css
            # i['last_reply_name'] = article.css
            # i['last_reply_time'] = article.css
            # i['reply_num'] = article.css
            yield i
