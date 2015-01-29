# -*- coding: utf-8 -*-

############################################
# Job Crawler - Regionjob crawler          #
# Created by RIVES Yann                    #
# Crawl Regionjob to find interesting jobs #
############################################

import bs4, datetime
from jobcrawler.core import toolbox
import logging

logger = logging.getLogger("jobcrawler")

class RegionjobCrawler(object):
    def __init__(self):
        self.websites = {"Toute la France":["www.centrejob.com","www.nordjob.com","www.pacajob.com","www.rhonealpesjob.com",
                                            "www.sudouestjob.com","www.parisjob.com","www.ouestjob.com","www.estjob.com"],
                         "Auvergne":["www.centrejob.com"],
                         "Centre":["www.centrejob.com"],
                         "Limousin":["www.centrejob.com"],
                         "Haute-Normandie":["www.nordjob.com"],
                         "Nord-Pas-de-Calais":["www.nordjob.com"],
                         "Picardie":["www.nordjob.com"],
                         "Languedoc-Roussillon":["www.pacajob.com"],
                         "PACA":["www.pacajob.com"],
                         "Rhône-Alpes":["www.rhonealpesjob.com"],
                         "Aquitaine":["www.sudouestjob.com"],
                         "Midi-Pyrénées":["www.sudouestjob.com"],
                         "Ile-de-France":["www.parisjob.com"],
                         "Basse-Normandie":["www.ouestjob.com"],
                         "Bretagne":["www.ouestjob.com"],
                         "Pays de la Loire":["www.ouestjob.com"],
                         "Poitou-Charentes":["www.ouestjob.com"],
                         "Alsace":["www.estjob.com"],
                         "Bourgogne":["www.estjob.com"],
                         "Champagne-Ardenne":["www.estjob.com"],
                         "Franche-Comté":["www.estjob.com"],
                         "Lorraine":["www.estjob.com"]}
        
        self.uris = {"Engineering":"/emplois/recherche.html?f=Ingenierie_meca_aero&c=CDI",
                     "Info-Hardware":"/emplois/recherche.html?f=Informatique_dev_hard&c=CDI",
                     "Info-Helpdesk":"/emplois/recherche.html?f=SAV_Hotline&c=CDI",
                     "Info-Software":"/emplois/recherche.html?f=Informatique_dev&c=CDI"}
    
    def _regionjob_crawler_common(self, webdomain, domain, daterange):
        """Common part for crawler regions"""
        

    def _regionjob_crawler(self, domain, daterange, region):
        """Crawler for Region job"""
        site_list = []
        webdomains = self.websites[region]
        
        for webdomain in webdomains:
            if not toolbox.ping_website(webdomain):
                logger.error("{0} not responding".format(webdomain))
                break
            
            uri = self.uris[domain]          
    
            soup = bs4.BeautifulSoup(toolbox.html_reader(webdomain,uri))
            # for each annonce section
            for annonce in soup.find_all('section', {'class': 'annonce'}):
                # Link is in the second <a> markup
                link = annonce.findAll('a')[1].get('href')
                date = annonce.findNext('p', {"class": "infos"}).contents[0].strip()
                
                try:
                    fmt = "%d/%m/%y"
                    date = datetime.datetime.strptime(date, fmt).date()
                except:
                    date = datetime.date.today()
                    
                if toolbox.compute_duration(date) < daterange:
                    site_list.append("http://{0}{1}".format(webdomain,link))
            
    
            site_list = list(set(site_list))
        
        return site_list

    def run_program(self, domain, daterange, region):
        """Method to run program"""
        regionjob_result = self._regionjob_crawler(domain, daterange, region)

        return regionjob_result
