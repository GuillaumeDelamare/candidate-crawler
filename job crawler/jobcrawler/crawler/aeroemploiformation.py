# -*- coding: utf-8 -*-

######################################################
# Job Crawler - Aeroemploiformation crawler          #
# Created by RIVES Yann                              #
# Crawl Aeroemploiformation to find interesting jobs #
######################################################

### External modules importation ###

import re
import bs4

### End of external modules importation ###

### Custom modules importation ###

from jobcrawler.core import toolbox

### End of custom modules importation ###

### Classes ###
class AeroemploiformationCrawler(object):

    def _aeroemploiformation_crawler(self, domain, region):
        """Crawler for Aero emploi formation"""
        site_list = []
        webdomain = "www.aeroemploiformation.com"

        if not toolbox.ping_website(webdomain):
            print("{0} not responding".format(webdomain))
            return

        if region == "Toute la France":
            region_code = ""
        elif region == "Alsace":
            region_code = "+region%3A42"
        elif region == "Aquitaine":
            region_code = "+region%3A72"
        elif region == "Auvergne":
            region_code = "+region%3A83"
        elif region == "Basse-Normandie":
            region_code = "+region%3A25"
        elif region == "Bourgogne":
            region_code = "+region%3A26"
        elif region == "Bretagne":
            region_code = "+region%3A53"
        elif region == "Centre":
            region_code = "+region%3A24"
        elif region == "Champagne-Ardenne":
            region_code = "+region%3A21"
        elif region == "Franche-Comté":
            region_code = "+region%3A43"
        elif region == "Haute-Normandie":
            region_code = "+region%3A23"
        elif region == "Ile-de-France":
            region_code = "+region%3A11"
        elif region == "Languedoc-Roussillon":
            region_code = "+region%3A91"
        elif region == "Limousin":
            region_code = "+region%3A74"
        elif region == "Lorraine":
            region_code = "+region%3A41"
        elif region == "Midi-Pyrénées":
            region_code = "+region%3A73"
        elif region == "Nord-Pas-de-Calais":
            region_code = "+region%3A31"
        elif region == "Pays de la Loire":
            region_code = "+region%3A52"
        elif region == "Picardie":
            region_code = "+region%3A22"
        elif region == "Poitou-Charentes":
            region_code = "+region%3A54"
        elif region == "PACA":
            region_code = "+region%3A93"
        elif region == "Rhône-Alpes":
            region_code = "+region%3A82"

        if domain == "Engineering" or domain == "Info-Hardware" or domain == "Info-Software":
            uri = "/candidate/offers/candidateOffersSearchResults.mj?q=contract-type%3ACDI{0}+macro-job%3A65+published-since%3A7&cid=189061".format(region_code)
        elif domain == "Info-Helpdesk":
            uri = "/candidate/offers/candidateOffersSearchResults.mj?q=contract-type%3ACDI{0}+macro-job%3A68+published-since%3A7&cid=189061".format(region_code)
        soup = bs4.BeautifulSoup(toolbox.html_reader(webdomain,uri))
        for link in soup.find_all(href=re.compile("offre-d-emploi")):
            link = link.get("href")
            site_list.append("http://{0}{1}".format(webdomain,link))

        site_list = list(set(site_list))

        return site_list

    def run_program(self, domain="Engineering", region="Midi-Pyrénées"):
        """Method to run program"""
        print("Crawling Aeroemploiformation ...")

        aeroemploiformation_result = self._aeroemploiformation_crawler(domain, region)

        print("Aeroemploiformation crawled")

        return aeroemploiformation_result

### End of Classes ###

### Main program ###

if __name__=='__main__':
    runapp = AeroemploiformationCrawler()
    print(runapp.run_program())

### End of Main program ###
