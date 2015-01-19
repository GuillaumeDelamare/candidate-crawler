# -*- coding: utf-8 -*-

#######################################
# Job Crawler - Apec crawler          #
# Created by RIVES Yann               #
# Crawl Apec to find interesting jobs #
#######################################

import re, bs4
from jobcrawler.core import toolbox
from datetime import datetime

class ApecCrawler(object):
    def __init__(self):
        self.webdomain = "cadres.apec.fr"
        self.regions = {"Toute la France": "",
                        "Alsace": "&region=700",
                        "Aquitaine": "&region=701",
                        "Auvergne": "&region=702",
                        "Basse-Normandie": "&region=703",
                        "Bourgogne": "&region=704",
                        "Bretagne": "&region=705",
                        "Centre": "&region=706",
                        "Champagne-Ardenne": "&region=707",
                        "Franche-Comté": "&region=709",
                        "Haute-Normandie": "&region=710",
                        "Ile-de-France": "&region=711",
                        "Languedoc-Roussillon": "&region=712",
                        "Limousin": "&region=713",
                        "Lorraine": "&region=714",
                        "Midi-Pyrénées": "&region=715",
                        "Nord-Pas-de-Calais": "&region=716",
                        "Pays de la Loire": "&region=717",
                        "Picardie": "&region=718",
                        "Poitou-Charentes": "&region=719",
                        "PACA": "&region=720",
                        "Rhône-Alpes": "&region=721"}

    def _apec_crawler(self, keywords, daterange, region):
        """Crawler for APEC"""
        site_list = []

        if not toolbox.ping_website(self.webdomain):
            print("{0} not responding".format(self.webdomain))
            return

        region_code = self.regions[region]
       
        for keyword in keywords:
            uri = u"/MesOffres/RechercheOffres/ApecRechercheOffre.jsp?keywords={0}{1}".format(keyword, region_code)
            soup = bs4.BeautifulSoup(toolbox.html_reader(self.webdomain,uri))
            for link in soup.find_all(href=re.compile("offre-d-emploi-")):
                pubtag = link.findNext("strong")
                try:
                    fmt = "Parue le %d/%m/%y"
                    pubdate = pubtag.contents[0]
                    pubdate = datetime.strptime(pubdate[:17], fmt).date()
                except:
                    pubdate = datetime.date.today()
                    
                link = re.sub(("\?(.*?)$"),'',link.get("href"))
                print(link)
                if toolbox.compute_duration(pubdate) < daterange:
                    print("added")
                    site_list.append("http://{0}{1}".format(self.webdomain,link))

        site_list = list(set(site_list))

        return site_list

    def run_program(self,keywords, daterange, region):
        """Method to run program"""
        apec_result = self._apec_crawler(keywords, daterange, region)
        return apec_result


if __name__=='__main__':
    runapp = ApecCrawler()
    print(runapp.run_program(["Java"], 3, "Pays de la Loire"))
