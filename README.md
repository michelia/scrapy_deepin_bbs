# scrapy_deepin_bbs
用scrapy采集[Deepin论坛](http://bbs.deepin.org/)列表信息(测试)  
顺便推广下Deepin  
[Deepin](http://www.deepin.org/)是非常好用的中文linux发行版，本人日常使用的系统。  

# 创建scrapy_deepin_bbs的过程

## 创建项目框架
`scrapy startproject scrapy_deepin_bbs`

## 根据sprider模板(crawl)，创建deepin_bbs
`scrapy genspider -t crawl  deepin_bbs bbs.deepin.org`

## 编辑ScrapyDeepinBbsItem和DeepinBbsSpider

## 编辑ScrapyDeepinBbsPipeline

## 建立代理中间组件RandomUserAgentMiddleware和ProxyMiddleware

## 配置settings
DOWNLOAD_DELAY  
COOKIES_ENABLED  
DOWNLOADER_MIDDLEWARES  
ITEM_PIPELINES  
以及代理需要的参数  
