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

            i['article_title'] = article.css('td.common a.xst::text').extract()[0]
            i['article_id'] = article.css('td.common a.xst::attr(href)').re(r'tid=(\d+)')[0]
            i['forum_plate'] = article.css('div.forum a::text').extract()[0]
            i['author_name'] = article.css('div.author cite a::text').extract()[0]
            try:
                i['post_date'] = article.css('div.z span span::attr(title)').extract()[0]
                i['last_reply_time'] = article.css('div.last-reply div.z span.z a span::attr(title)').extract()[0]
            except IndexError, e:
                print e
                i['post_date'] = article.css('td.article-info div.z span::text').extract()[0].strip()
                i['last_reply_time'] = article.css('div.last-reply div.z span.z a::text').extract()[0].strip()
            i['last_reply_name'] = article.css('div.last-reply cite a::text').extract()[0].strip()
            i['reply_num'] = article.css('div.replies a::text').extract()[0].strip()
            yield i
