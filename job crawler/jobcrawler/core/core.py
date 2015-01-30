# -*- coding: utf-8 -*-


import urllib, bs4, re, logging
from jobcrawler.core import dbmanagement
from jobcrawler.crawler import apec, caoemploi, indeed, monster, poleemploi,\
    regionjob
    
logger = logging.getLogger("jobcrawler")

class core(object):
    def __init__(self, dbpath):
        self.dbpath = dbpath
    
    def exclude_annouces(self, excludelist):
        db = dbmanagement.database(self.dbpath)
        temp = db.ads
        db.ads = []
        
        for ad in temp:
            try:
                htmlpage = urllib.urlopen(ad.link).read()
                soup = bs4.BeautifulSoup(htmlpage)
                
                word_found = False
                for word in excludelist:
                    if soup.body.find_all(text=re.compile(word, re.IGNORECASE)) != []:
                        word_found = True
                
                if not word_found:
                    db.ads.append(ad)
 
            except Exception as e:
                logger.error("Error on link {0}".format(ad.link))
                logger.debug(e)
                
        db.merge()
        db.write()
        
    def filter_announces(self, wordslist):
        db = dbmanagement.database(self.dbpath)
        temp = db.ads
        db.ads = []
        
        for ad in temp:
            try:
                htmlpage = urllib.urlopen(ad.link).read()
                soup = bs4.BeautifulSoup(htmlpage)
 
                for word in wordslist:
                    if soup.body.find_all(text=re.compile(word, re.IGNORECASE)) != []:
                        ad.filterkeywords.append(word)
                
                if len(ad.filterkeywords) > 0:
                    db.ads.append(ad)
 
            except Exception as e:
                logger.error("Error on link {0}".format(ad.link))
                logger.debug(e)
        
        db.merge()
        db.write()
    
    def found_annonce(self, keywords, daterange, region, domain, apecc=False, caoec=False, ic=False, mc=False, poc=False, rjc=False):
        db = dbmanagement.database(self.dbpath)
        
        if apecc:
            logger.info(u"Recherche d'annonce sur l'APEC")
            apec.ApecCrawler().run_program(keywords,daterange,region)
        if caoec:
            logger.info(u"Recherche d'annonce sur CAO emploi")
            caoemploi.CaoemploiCrawler().run_program(region)
        if ic:
            logger.info(u"Recherche d'annonce sur Indeed")
            indeed.IndeedCrawler(db).run(keywords,daterange,region)
        if mc:
            logger.info(u"Recherche d'annonce sur Monster job")
            monster.MonsterCrawler().run_program(keywords,daterange,region)
        if poc:
            logger.info(u"Recherche d'annonce sur Pôle emploi")
            poleemploi.PoleemploiCrawler().run_program(keywords,daterange,region)
        if rjc:
            logger.info(u"Recherche d'annonce sur Région job")
            regionjob.RegionjobCrawler().run_program(domain,daterange,region)
        
        db.merge()
        db.write()



if __name__=='__main__':
    runapp = core("./db.csv")
    logger.info("Found announces")
    runapp.found_annonce([u"Ingénieur"], 6, "Pays de la Loire", "toto", ic=True)
    logger.info("Done")
    logger.info("Exclude announces")
    runapp.exclude_annouces([u"interim", u"intérim", u"commercial"])
    logger.info("Done")
    logger.info("Filter announces")
    runapp.filter_announces([u"Ingénieur"])
    logger.info("Done")
