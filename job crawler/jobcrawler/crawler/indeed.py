# -*- coding: utf-8 -*-

#########################################
# Job Crawler - Indeed crawler          #
# Created by RIVES Yann                 #
# Crawl Indeed to find interesting jobs #
#########################################

### External modules importation ###

import re
import bs4

### End of external modules importation ###

### Custom modules importation ###

from jobcrawler.core import toolbox

### End of custom modules importation ###

### Classes ###
class IndeedCrawler(object):

    def _indeed_crawler(self, keywords, daterange, region):
        """Crawler for Indeed"""
        site_list = []
        webdomain = "www.indeed.fr"

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
            region_code = "Basse-Normandie"
        elif region == "Bourgogne":
            region_code = "Bourgogne"
        elif region == "Bretagne":
            region_code = "Bretagne"
        elif region == "Centre":
            region_code = "Centre"
        elif region == "Champagne-Ardenne":
            region_code = "Champagne-Ardenne"
        elif region == "Franche-Comté":
            region_code = "Franche-Comt%C3%A9"
        elif region == "Haute-Normandie":
            region_code = "Haute-Normandie"
        elif region == "Ile-de-France":
            region_code = "%C3%8Ele-de-France"
        elif region == "Languedoc-Roussillon":
            region_code = "Languedoc-Roussillon"
        elif region == "Limousin":
            region_code = "Limousin"
        elif region == "Lorraine":
            region_code = "Lorraine"
        elif region == "Midi-Pyrénées":
            region_code = "Midi-Pyr%C3%A9n%C3%A9es"
        elif region == "Nord-Pas-de-Calais":
            region_code = "Nord-Pas+de+Calais"
        elif region == "Pays de la Loire":
            region_code = "Pays+de+la+Loire"
        elif region == "Picardie":
            region_code = "Picardie"
        elif region == "Poitou-Charentes":
            region_code = "Poitou-Charentes"
        elif region == "PACA":
            region_code = "Provence-Alpes-C%C3%B4te+d%27Azur"
        elif region == "Rhône-Alpes":
            region_code = "Rh%C3%B4ne-Alpes"

        for keyword in keywords:
            uri = "/emplois?as_and={0}&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&sr=directhire&radius=0&l={1}&fromage={2}&limit=50&sort=date&psf=advsrch".format(keyword, region_code, daterange)
            soup = bs4.BeautifulSoup(toolbox.html_reader(webdomain,uri))
            for link in soup.find_all(href=re.compile("/rc/")):
                link = link.get("href")
                site_list.append("http://{0}{1}".format(webdomain,link))

        site_list = list(set(site_list))

        return site_list

    def run_program(self,keywords=("dessinateur","catia"), daterange=3, region="Midi-Pyrénées"):
        """Method to run program"""
        print("Crawling Indeed ...")

        indeed_result = self._indeed_crawler(keywords, daterange, region)

        print("Indeed crawled")

        return indeed_result

### End of Classes ###

### Main program ###

if __name__=='__main__':
    runapp = IndeedCrawler()
    print(runapp.run_program())

### End of Main program ###
