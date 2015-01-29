# -*- coding: utf-8 -*-

##########################################
# Job Crawler - Monster crawler          #
# Created by RIVES Yann                  #
# Crawl Monster to find interesting jobs #
##########################################

### External modules importation ###

import re, bs4
from jobcrawler.core import toolbox
import logging

logger = logging.getLogger("jobcrawler")

class MonsterCrawler(object):
    def __init__(self):
        self.webdomain = "offres.monster.fr"
        self.regions = {"Toute la France": "France",
                        "Alsace": "Alsace",
                        "Aquitaine": "Aquitaine",
                        "Auvergne": "Auvergne",
                        "Basse-Normandie": "Basse__2DNormandie",
                        "Bourgogne": "Bourgogne",
                        "Bretagne": "Bretagne",
                        "Centre": "Centre",
                        "Champagne-Ardenne": "Champagne__2DArdenne",
                        "Franche-Comté": "Franche__2DComt__C3__A9",
                        "Haute-Normandie": "Haute__2DNormandie",
                        "Ile-de-France": "Ile__2Dde__2DFrance",
                        "Languedoc-Roussillon": "Languedoc__2DRoussillon",
                        "Limousin": "Limousin",
                        "Lorraine": "Lorraine",
                        "Midi-Pyrénées": "Midi__2DPyr__C3__A9n__C3__A9es",
                        "Nord-Pas-de-Calais": "Nord__2DPas__2Dde__2DCalais",
                        "Pays de la Loire": "Pays-de-la-Loire",
                        "Picardie": "Picardie",
                        "Poitou-Charentes": "Poitou__2DCharentes",
                        "PACA": "Provence__2DAlpes__2DC__C3__B4te-d__27Azur",
                        "Rhône-Alpes": "Rh__C3__B4ne__2DAlpes"}

    def _monster_crawler(self, keywords, daterange, region):
        """Crawler for Monster"""
        site_list = []

        if not toolbox.ping_website(self.webdomain):
            logger.error("{0} not responding".format(self.webdomain))
            return

        region_code = self.regions[region]

        for keyword in keywords:
            uri = "/offres-d-emploi/?tm={1}&q={0}&where={2}".format(keyword, daterange, region_code)
            soup = bs4.BeautifulSoup(toolbox.html_reader(self.webdomain, uri))
            
            for link in soup.find_all(href=re.compile("offre-emploi")):
                site_list.append(link.get("href"))

        site_list = list(set(site_list))

        return site_list

    def run_program(self, keywords, daterange, region):
        """Method to run program"""
        monster_result = self._monster_crawler(keywords, daterange, region)

        return monster_result
