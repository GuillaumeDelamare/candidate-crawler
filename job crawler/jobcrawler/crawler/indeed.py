# -*- coding: utf-8 -*-

#########################################
# Job Crawler - Indeed crawler          #
# Created by RIVES Yann                 #
# Crawl Indeed to find interesting jobs #
#########################################

import bs4, logging
from jobcrawler.core import toolbox, dbmanagement
from jobcrawler.crawler.defaultcrawler import defaultCrawler
from datetime import datetime, timedelta
from unidecode import unidecode

logger = logging.getLogger("jobcrawler")

class IndeedCrawler(defaultCrawler):
    def __init__(self, database):
        defaultCrawler.__init__(self, database, "www.indeed.fr")
        self.regions = {"Toute la France": "France",
                        "Alsace":"Alsace",
                        "Aquitaine": "Aquitaine",
                        "Auvergne": "Auvergne",
                        "Basse-Normandie": "Basse-Normandie",
                        "Bourgogne": "Bourgogne",
                        "Bretagne": "Bretagne",
                        "Centre": "Centre",
                        "Champagne-Ardenne": "Champagne-Ardenne",
                        "Franche-Comté": "Franche-Comt%C3%A9",
                        "Haute-Normandie": "Haute-Normandie",
                        "Ile-de-France": "%C3%8Ele-de-France",
                        "Languedoc-Roussillon": "Languedoc-Roussillon",
                        "Limousin": "Limousin",
                        "Lorraine": "Lorraine",
                        "Midi-Pyrénées": "Midi-Pyr%C3%A9n%C3%A9es",
                        "Nord-Pas-de-Calais": "Nord-Pas+de+Calais",
                        "Pays de la Loire": "Pays+de+la+Loire",
                        "Picardie": "Picardie",
                        "Poitou-Charentes": "Poitou-Charentes",
                        "PACA": "Provence-Alpes-C%C3%B4te+d%27Azur",
                        "Rhône-Alpes": "Rh%C3%B4ne-Alpes"}

    def run(self, keywords, daterange, region):
        defaultCrawler.run(self)
        
        region_code = self.regions[region]

        for keyword in keywords:
            uri = u"/emplois?as_and={0}&l={1}&fromage={2}&limit=50&sort=date&psf=advsrch".format(keyword, region_code, daterange)
            soup = bs4.BeautifulSoup(toolbox.html_reader(self.webdomain,uri))
            logger.debug(uri)
            for annonce in soup.find_all('div', {'class': 'row  result'}):
                link = "http://{0}{1}".format(self.webdomain, annonce.find('a').get('href'))
                
                try:
                    temp = annonce.find('span', {'class': 'company'})
                    temp = temp.find('span')
                    firm = ""
                    for s in temp.contents:
                        try:
                            firm += s
                        except:
                            pass
                    
                    firm = unidecode(firm)
                
                except:
                    firm = "Inconnu"
                    
                try:
                    temp = annonce.find('h2', {'class': 'jobtitle'})
                    temp = temp.find('a')
                    title = ""
                    for s in temp.contents:
                        try:
                            title += s
                        except:
                            pass
                    
                    title = unidecode(title)
                except:
                    title = "Inconnu"
                
                try:
                    temp = annonce.find('span', {'class', 'date'})
                    releasedate = temp.contents[0].encode("utf-8")
                    
                    if "heure" in releasedate:
                        releasedate = datetime.now()
                    elif "jour" in releasedate:
                        releasedate = datetime.now() - timedelta(int(releasedate.split()[3]))
                    else:
                        releasedate = None
                except:
                    releasedate = None
                    
                self.database.ads.append(dbmanagement.ad(link=link, 
                                                         founddate=datetime.now(),
                                                         releasedate=releasedate,
                                                         searchkeywords=[keyword],
                                                         firm=firm,
                                                         title=title))
