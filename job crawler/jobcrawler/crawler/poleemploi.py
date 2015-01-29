# -*- coding: utf-8 -*-

##############################################
# Job Crawler - Pole emploi crawler          #
# Created by RIVES Yann                      #
# Crawl Pole emploi to find interesting jobs #
##############################################

import re, bs4
from jobcrawler.core import toolbox
import logging

logger = logging.getLogger("jobcrawler")

class PoleemploiCrawler(object):
    def __init__(self):
        self.webdomain = "candidat.pole-emploi.fr"
        self.regions = {"Toute la France": "PAYS_01",
                        "Alsace": "REGION_42",
                        "Aquitaine": "REGION_72",
                        "Auvergne": "REGION_83",
                        "Basse-Normandie": "REGION_25",
                        "Bourgogne": "REGION_26",
                        "Bretagne": "REGION_53",
                        "Centre": "REGION_24",
                        "Champagne-Ardenne": "REGION_21",
                        "Franche-Comté": "REGION_43",
                        "Haute-Normandie": "REGION_23",
                        "Ile-de-France": "REGION_11",
                        "Languedoc-Roussillon": "REGION_91",
                        "Limousin": "REGION_74",
                        "Lorraine": "REGION_41",
                        "Midi-Pyrénées": "REGION_73",
                        "Nord-Pas-de-Calais": "REGION_31",
                        "Pays de la Loire": "REGION_52",
                        "Picardie": "REGION_22",
                        "Poitou-Charentes": "REGION_54",
                        "PACA": "REGION_93",
                        "Rhône-Alpes": "REGION_82"}

    def _poleemploi_crawler(self, keywords, daterange, region):
        """Crawler for Pole emploi"""
        site_list = []
        
        if not toolbox.ping_website(self.webdomain):
            logger.error("{0} not responding".format(self.webdomain))
            return

        region_code = self.regions[region]

        for keyword in keywords:
            uri = "/candidat/rechercheoffres/resultats/A__{1}___P________{0}__INDIFFERENT______________{2}___".format(keyword, region_code, daterange)
            soup = bs4.BeautifulSoup(toolbox.html_reader(self.webdomain,uri))
            for link in soup.find_all(href=re.compile("rechercheoffres")):
                link = re.sub(("\;(.*?)$"),'',link.get("href")).replace("resultats.composantresultatrechercheoffre.tableauresultatrechercheoffre:detailoffre","detail")
                site_list.append("http://{0}{1}".format(self.webdomain,link))

        site_list = list(set(site_list))

        return site_list

    def run_program(self,keywords, daterange, region):
        """Method to run program"""
        poleemploi_result = self._poleemploi_crawler(keywords, daterange, region)

        return poleemploi_result
