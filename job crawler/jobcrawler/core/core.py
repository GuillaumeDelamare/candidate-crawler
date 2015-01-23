# -*- coding: utf-8 -*-

###############################################
# Job Crawler - Core program                  #
# Created by RIVES Yann                       #
# Crawl some website to find interesting jobs #
###############################################

from jobcrawler.core import dbmanagement
import threading
from jobcrawler.crawler import apec, caoemploi, indeed, monster, poleemploi,\
    regionjob

class JobCrawlerCore(object):
    def __init__(self, dbfile, exclude_list, max_store_day=40):
        self.dbfile = dbfile
        self.exclude_list = exclude_list
        self.max_store_day = max_store_day
 
    def _values_initializer(self):
        """Method to initialize variables"""
        self.newlinks_list = []
        self.final_links_list = []
         
    def _links_management(self, linklist, queries):
        """Method to manage links in global list"""
        # Filter the link already in the database
        linklist = list(set(linklist))
        database = dbmanagement.read_database(self.dbfile, "links")
        func = lambda link: link not in database
        filtered_linklist = filter(func, linklist)
 
        # Test the content of the link
        for link in filtered_linklist:
            error_code = False
 
            try:
                htmlpage = urllib.urlopen(link).read()
                soup = bs4.BeautifulSoup(htmlpage)
 
                if self.exclude_list[0] != "":
                    for word in self.exclude_list:
                        if soup.body.find_all(text=re.compile(word, re.IGNORECASE)) != []:
                            error_code = True
                            break
 
                if queries[0] != "" and not error_code:
                    criteria_found = False
                    for word in queries:
                        if soup.body.find_all(text=re.compile(word, re.IGNORECASE)) != []:
                            criteria_found = True
                            break
 
                    if not criteria_found:
                        error_code = True
 
            except Exception as e:
                error_code = True
                print("Error on link {0}".format(link))
                print(e)
 
            if not error_code:
                self.final_links_list.append(link)
 
    def run_program(self, acc=True, aefc=True, apecc=True, caoec=True, ic=True, mc=True, poc=True, rjc=True,\
                    domain="Engineering", keywords=("dessinateur","catia"), queries=("catia","meca"), region="Midi-Pyrénées",\
                    daterange=3, db_management=False):
        """Method to run program"""
        self._values_initializer()
 
        if acc:
            runacc = aerocontact.AerocontactCrawler()
            for link in runacc.run_program(keywords,daterange,region):
                self.newlinks_list.append(link)
        if aefc:
            runaefc = aeroemploiformation.AeroemploiformationCrawler()
            for link in runaefc.run_program(domain,region):
                self.newlinks_list.append(link)
        if apecc:
            runapecc = apec.ApecCrawler()
            for link in runapecc.run_program(keywords,daterange,region):
                self.newlinks_list.append(link)
        if caoec:
            runcaoec = caoemploi.CaoemploiCrawler()
            for link in runcaoec.run_program(region):
                self.newlinks_list.append(link)
        if ic:
            runic = indeed.IndeedCrawler()
            for link in runic.run_program(keywords,daterange,region):
                self.newlinks_list.append(link)
        if mc:
            runmc = monster.MonsterCrawler()
            for link in runmc.run_program(keywords,daterange,region):
                self.newlinks_list.append(link)
        if poc:
            runpoc = poleemploi.PoleemploiCrawler()
            for link in runpoc.run_program(keywords,daterange,region):
                self.newlinks_list.append(link)
        if rjc:
            runrjc = regionjob.RegionjobCrawler()
            for link in runrjc.run_program(domain,daterange,region):
                self.newlinks_list.append(link)
 
        self._links_management(self.newlinks_list, queries)
 
        if db_management:
            dbmanagement.write_database(self.dbfile, self.final_links_list)
            dbmanagement.clean_database(self.dbfile, self.max_store_day)
 
        return self.final_links_list



class core(threading.Thread):
    def __init__(self, dbpath, exclude_list, keywords, daterange, region, queries, domain, max_store_day=40,
                 apecc=False, caoec=False, ic=False, mc=False, poc=False, rjc=False):
        threading.Thread.__init__(self)
        self.dbpath = dbpath
        self.exclude_list = exclude_list
        self.keywords = keywords
        self.daterange = daterange
        self.region = region
        self.queries = queries
        self.domain = domain
        self.max_store_day = max_store_day
        self.apecc = apecc
        self.caoec = caoec
        self.ic = ic
        self.mc = mc
        self.poc = poc
        self.rjc = rjc
        
    
    def run(self):
        threading.Thread.run(self)
        
        db = dbmanagement.database(self.dbpath)
        
        if self.apecc:
            apec.ApecCrawler().run_program(self.keywords,self.daterange,self.region)
        if self.caoec:
            caoemploi.CaoemploiCrawler().run_program(self.region)
        if self.ic:
            indeed.IndeedCrawler(db).run(self.keywords,self.daterange,self.region)
        if self.mc:
            monster.MonsterCrawler().run_program(self.keywords,self.daterange,self.region)
        if self.poc:
            poleemploi.PoleemploiCrawler().run_program(self.keywords,self.daterange,self.region)
        if self.rjc:
            regionjob.RegionjobCrawler().run_program(self.domain,self.daterange,self.region)
        
        db.merge()
        
        
        
        db.write()



if __name__=='__main__':
    runapp = core("./db.csv", ["interim", "intérim", "commercial"], ["Java"], 3, "Pays de la Loire", "toto", "toto", ic=True)
    runapp.start()
    
