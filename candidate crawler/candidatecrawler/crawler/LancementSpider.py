'''
Created on 12 janv. 2015

@author: Jonathan
'''

from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log
from candidatecrawler.crawler.apecSelenium import apecSelenium

spider = apecSelenium('47179308','6KPA43V8','catia',["France Outre-Mer","Franche-Comte","Haute-Normandie","Ile-de-France","Languedoc-Roussillon"],"","","","",50)
crawler = Crawler(Settings())
crawler.configure()
crawler.crawl(spider)
crawler.start()
log.start()


reactor.run() #@UndefinedVariable