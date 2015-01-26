# -*- coding: utf-8 -*-


import urllib, bs4, re
from jobcrawler.core import dbmanagement
from jobcrawler.crawler import apec, caoemploi, indeed, monster, poleemploi,\
    regionjob

class core(object):
    def __init__(self, dbpath):
        self.dbpath = dbpath
    
    def exclude_annouces(self, excludelist):
        db = dbmanagement.database(self.dbpath)
        temp = db.ads
        db.ads = []
        
        for ad in temp:
            print("Treat this announce : {}".format(ad.link))
            try:
                htmlpage = urllib.urlopen(ad.link).read()
                soup = bs4.BeautifulSoup(htmlpage)
                
                word_found = False
                for word in excludelist:
                    print("    Search this word {}".format(word))
                    if soup.body.find_all(text=re.compile(word, re.IGNORECASE)) != []:
                        word_found = True
                
                if not word_found:
                    db.ads.append(ad)
 
            except Exception as e:
                print("Error on link {0}".format(ad.link))
                print(e)
                
        db.merge()
        db.write()
        
    def filter_announces(self, wordslist):
        db = dbmanagement.database(self.dbpath)
        temp = db.ads
        db.ads = []
        
        for ad in temp:
            print("Treat this announce : {}".format(ad.link))
            try:
                htmlpage = urllib.urlopen(ad.link).read()
                soup = bs4.BeautifulSoup(htmlpage)
 
                for word in wordslist:
                    print("    Search this word {}".format(word))
                    if soup.body.find_all(text=re.compile(word, re.IGNORECASE)) != []:
                        ad.filterkeywords.append(word)
                
                if len(ad.filterkeywords) > 0:
                    db.ads.append(ad)
 
            except Exception as e:
                print("Error on link {0}".format(ad.link))
                print(e)
        
        db.merge()
        db.write()
    
    def found_annonce(self, keywords, daterange, region, domain, apecc=False, caoec=False, ic=False, mc=False, poc=False, rjc=False):
        db = dbmanagement.database(self.dbpath)
        
        if apecc:
            apec.ApecCrawler().run_program(keywords,daterange,region)
        if caoec:
            caoemploi.CaoemploiCrawler().run_program(region)
        if ic:
            indeed.IndeedCrawler(db).run(keywords,daterange,region)
        if mc:
            monster.MonsterCrawler().run_program(keywords,daterange,region)
        if poc:
            poleemploi.PoleemploiCrawler().run_program(keywords,daterange,region)
        if rjc:
            regionjob.RegionjobCrawler().run_program(domain,daterange,region)
        
        db.merge()
        db.write()



if __name__=='__main__':
    runapp = core("./db.csv")
    print("Found announces")
    runapp.found_annonce(["Ingenieur","Developpement","logiciel","Python","Java","Script","Bash", "C"], 7, "Pays de la Loire", "toto", ic=True)
    print("Done")
    print("Exclude announces")
    runapp.exclude_annouces(["interim", "intérim", "commercial"])
    print("Done")
    print("Filter announces")
    runapp.filter_announces(["Python","Java","Script","Bash", "C"])
    print("Done")
