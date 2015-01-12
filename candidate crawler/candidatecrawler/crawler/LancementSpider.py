'''
Created on 12 janv. 2015

@author: Jonathan
'''

from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log
from candidatecrawler.crawler.apec import CVSpider

spider = CVSpider('','','')
crawler = Crawler(Settings())
crawler.configure()
crawler.crawl(spider)
crawler.start()
log.start()


reactor.run() #@UndefinedVariable