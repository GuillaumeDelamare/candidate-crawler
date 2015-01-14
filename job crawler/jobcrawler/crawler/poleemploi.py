# -*- coding: utf-8 -*-

##############################################
# Job Crawler - Pole emploi crawler          #
# Created by RIVES Yann                      #
# Crawl Pole emploi to find interesting jobs #
##############################################

### External modules importation ###

import re
import bs4

### End of external modules importation ###

### Custom modules importation ###

from jobcrawler.core import toolbox

### End of custom modules importation ###

### Classes ###
class PoleemploiCrawler(object):

    def _poleemploi_crawler(self, keywords, daterange, region):
        """Crawler for Pole emploi"""
        site_list = []
        webdomain = "candidat.pole-emploi.fr"

        if not toolbox.ping_website(webdomain):
            print("{0} not responding".format(webdomain))
            return

        if region == "Toute la France":
            region_code = "PAYS_01"
        elif region == "Alsace":
            region_code = "REGION_42"
        elif region == "Aquitaine":
            region_code = "REGION_72"
        elif region == "Auvergne":
            region_code = "REGION_83"
        elif region == "Basse-Normandie":
            region_code = "REGION_25"
        elif region == "Bourgogne":
            region_code = "REGION_26"
        elif region == "Bretagne":
            region_code = "REGION_53"
        elif region == "Centre":
            region_code = "REGION_24"
        elif region == "Champagne-Ardenne":
            region_code = "REGION_21"
        elif region == "Franche-Comté":
            region_code = "REGION_43"
        elif region == "Haute-Normandie":
            region_code = "REGION_23"
        elif region == "Ile-de-France":
            region_code = "REGION_11"
        elif region == "Languedoc-Roussillon":
            region_code = "REGION_91"
        elif region == "Limousin":
            region_code = "REGION_74"
        elif region == "Lorraine":
            region_code = "REGION_41"
        elif region == "Midi-Pyrénées":
            region_code = "REGION_73"
        elif region == "Nord-Pas-de-Calais":
            region_code = "REGION_31"
        elif region == "Pays de la Loire":
            region_code = "REGION_52"
        elif region == "Picardie":
            region_code = "REGION_22"
        elif region == "Poitou-Charentes":
            region_code = "REGION_54"
        elif region == "PACA":
            region_code = "REGION_93"
        elif region == "Rhône-Alpes":
            region_code = "REGION_82"

        for keyword in keywords:
            uri = "/candidat/rechercheoffres/resultats/A_{0}_{1}__11___________INDIFFERENT______________{2}".format(keyword, region_code, daterange)
            soup = bs4.BeautifulSoup(toolbox.html_reader(webdomain,uri))
            for link in soup.find_all(href=re.compile("rechercheoffres")):
                link = re.sub(("\;(.*?)$"),'',link.get("href")).replace("resultats.composantresultatrechercheoffre.tableauresultatrechercheoffre:detailoffre","detail")
                site_list.append("http://{0}{1}".format(webdomain,link))

        site_list = list(set(site_list))

        return site_list

    def run_program(self,keywords, daterange, region):
        """Method to run program"""
        poleemploi_result = self._poleemploi_crawler(keywords, daterange, region)

        return poleemploi_result

### End of Classes ###

### Main program ###

if __name__=='__main__':
    runapp = PoleemploiCrawler()
    print(runapp.run_program())

### End of Main program ###
