# -*- coding: utf-8 -*-
'''
Created on 7 janv. 2015

@author: Jonathan
'''

### Modules importation ###
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log
from candidatecrawler.crawler.apecSelenium import apecSelenium

### End modules importation ###

### Classes ###
class CandidateCrawlerCore(object):
    #TODO: Listeners
    keyword = ""
    region = []
    mobilite = ""
    salaire = ""
    disponibilite = ""
    fraicheur = ""
    nombreCV = 50 
    login =""
    password=""
    
    def __init__(self,login,password,keyword,region,mobilite,salaire,disponibilite,fraicheur,nombreCV):
        """Initialisation du spider"""
        
        self.keyword = keyword 
        self.region = region
        self.mobilite = mobilite
        self.salaire = salaire
        self.disponibilite = disponibilite
        self.fraicheur = fraicheur
        self.nombreCV = nombreCV
        self.login=login
        self.password=password
    
    
    
#     #TODO: Appel crawler
    def crawl(self):
        
#         print(login)
#         print(password)
#         print(keyword)
#         print(region)
#         print(mobilite)
#         print(salaire)
#         print(disponibilite)
#         print(fraicheur)
#         print(nombreCV)
        
        spider = apecSelenium(self.login,self.password,self.keyword,self.region,self.mobilite,self.salaire,self.disponibilite,self.fraicheur,self.nombreCV)
        spider.parse()
#         crawler = Crawler(Settings())
#         crawler.configure()
#         crawler.crawl(spider)
#         crawler.start()
#         log.start()
#         reactor.run() #@UndefinedVariable
        

    