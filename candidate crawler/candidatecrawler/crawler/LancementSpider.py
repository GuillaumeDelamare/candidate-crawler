# -*- coding: utf-8 -*-
'''
Created on 12 janv. 2015

@author: Jonathan
'''

from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log
from candidatecrawler.crawler.apecSelenium import apecSelenium
from candidatecrawler.core.core import CandidateCrawlerCore

#spider = apecSelenium('47179308','6KPA43V8','catia',["France Outre-Mer","Franche-Comté","Haute-Normandie","Ile-de-France","Languedoc-Roussillon"],0,5 ,['0','1','2'],2,50)


# crawler = Crawler(Settings())
# crawler.configure()
# crawler.crawl(spider)
# crawler.start()
# log.start()
#  
#  
# print(reactor.run()) #@UndefinedVariable
CandidateCrawlerCore('47179308','6KPA43V8','catia',["France Outre-Mer","Franche-Comté","Haute-Normandie","Ile-de-France","Languedoc-Roussillon"],0,5 ,['0','1','2'],2,50).crawl()

