# -*- coding: utf-8 -*-

##########################################
# Job Crawler - Monster crawler          #
# Created by RIVES Yann                  #
# Crawl Monster to find interesting jobs #
##########################################

### External modules importation ###

import re
import bs4

### End of external modules importation ###

### Custom modules importation ###

from jobcrawler.core import toolbox

### End of custom modules importation ###

### Classes ###
class MonsterCrawler(object):

    def _monster_crawler(self, keywords, daterange, region):
        """Crawler for Monster"""
        site_list = []
        webdomain = "offres.monster.fr"

        if not toolbox.ping_website(webdomain):
            print("{0} not responding".format(webdomain))
            return

        if region == "Toute la France":
            region_code = "France"
        elif region == "Alsace":
            region_code = "Alsace"
        elif region == "Aquitaine":
            region_code = "Aquitaine"
        elif region == "Auvergne":
            region_code = "Auvergne"
        elif region == "Basse-Normandie":
            region_code = "Basse__2DNormandie"
        elif region == "Bourgogne":
            region_code = "Bourgogne"
        elif region == "Bretagne":
            region_code = "Bretagne"
        elif region == "Centre":
            region_code = "Centre"
        elif region == "Champagne-Ardenne":
            region_code = "Champagne__2DArdenne"
        elif region == "Franche-Comté":
            region_code = "Franche__2DComt__C3__A9"
        elif region == "Haute-Normandie":
            region_code = "Haute__2DNormandie"
        elif region == "Ile-de-France":
            region_code = "Ile__2Dde__2DFrance"
        elif region == "Languedoc-Roussillon":
            region_code = "Languedoc__2DRoussillon"
        elif region == "Limousin":
            region_code = "Limousin"
        elif region == "Lorraine":
            region_code = "Lorraine"
        elif region == "Midi-Pyrénées":
            region_code = "Midi__2DPyr__C3__A9n__C3__A9es"
        elif region == "Nord-Pas-de-Calais":
            region_code = "Nord__2DPas__2Dde__2DCalais"
        elif region == "Pays de la Loire":
            region_code = "Pays-de-la-Loire"
        elif region == "Picardie":
            region_code = "Picardie"
        elif region == "Poitou-Charentes":
            region_code = "Poitou__2DCharentes"
        elif region == "PACA":
            region_code = "Provence__2DAlpes__2DC__C3__B4te-d__27Azur"
        elif region == "Rhône-Alpes":
            region_code = "Rh__C3__B4ne__2DAlpes"

        for keyword in keywords:
            uri = "/rechercher/{0}+CDI_548?tm={1}&where={2}".format(keyword, daterange, region_code)
            soup = bs4.BeautifulSoup(toolbox.html_reader(webdomain,uri))
            for link in soup.find_all(href=re.compile("offre-emploi")):
                link = link.get("href")
                site_list.append("{0}".format(link))

        site_list = list(set(site_list))

        return site_list

    def run_program(self,keywords=("dessinateur","catia"), daterange=3, region="Midi-Pyrénées"):
        """Method to run program"""
        print("Crawling Monster ...")

        monster_result = self._monster_crawler(keywords, daterange, region)

        print("Monster crawled")

        return monster_result

### End of Classes ###

### Main program ###

if __name__=='__main__':
    runapp = MonsterCrawler()
    print(runapp.run_program())

### End of Main program ###
