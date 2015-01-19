# -*- coding: utf-8 -*-

#########################################
# Job Crawler - Indeed crawler          #
# Created by RIVES Yann                 #
# Crawl Indeed to find interesting jobs #
#########################################

import re, bs4
from jobcrawler.core import toolbox

class IndeedCrawler(object):
    def __init__(self):
        self.webdomain = "www.indeed.fr"
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

    def _indeed_crawler(self, keywords, daterange, region):
        """Crawler for Indeed"""
        site_list = []

        if not toolbox.ping_website(self.webdomain):
            print("{0} not responding".format(self.webdomain))
            return

        region_code = self.regions[region]

        for keyword in keywords:
            uri = "/emplois?as_and={0}&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&sr=directhire&radius=0&l={1}&fromage={2}&limit=50&sort=date&psf=advsrch".format(keyword, region_code, daterange)
            soup = bs4.BeautifulSoup(toolbox.html_reader(self.webdomain,uri))
            for link in soup.find_all(href=re.compile("/rc/")):
                link = link.get("href")
                site_list.append("http://{0}{1}".format(self.webdomain,link))

        site_list = list(set(site_list))

        return site_list

    def run_program(self ,keywords, daterange, region):
        """Method to run program"""
        indeed_result = self._indeed_crawler(keywords, daterange, region)

        return indeed_result


if __name__=='__main__':
    runapp = IndeedCrawler()
    print(runapp.run_program(["Java"], 3, "Pays de la Loire"))
