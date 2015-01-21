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
    
    
    

    def crawl(self):
        

        spider = apecSelenium(self.login,self.password,self.keyword,self.region,self.mobilite,self.salaire,self.disponibilite,self.fraicheur,self.nombreCV)
        spider.parse()


    