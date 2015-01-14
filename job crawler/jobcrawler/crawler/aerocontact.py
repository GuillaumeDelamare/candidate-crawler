# -*- coding: utf-8 -*-

##############################################
# Job Crawler - Aerocontact crawler          #
# Created by RIVES Yann                      #
# Crawl Aerocontact to find interesting jobs #
##############################################

### External modules importation ###

import re
import bs4

### End of external modules importation ###

### Custom modules importation ###

from jobcrawler.core import toolbox

### End of custom modules importation ###

### Classes ###
class AerocontactCrawler(object):
    def _aerocontact_crawler(self, keywords, daterange, region):
        """Crawler for Aerocontact"""
        site_list = []
        webdomain = "www.aerocontact.com"

        if not toolbox.ping_website(webdomain):
            print("{0} not responding".format(webdomain))
            return

        if region == "Toute la France":
            region_code = "FRE"
        elif region == "Alsace":
            region_code = "FR01"
        elif region == "Aquitaine":
            region_code = "FR02"
        elif region == "Auvergne":
            region_code = "FR03"
        elif region == "Basse-Normandie":
            region_code = "FR16"
        elif region == "Bourgogne":
            region_code = "FR04"
        elif region == "Bretagne":
            region_code = "FR05"
        elif region == "Centre":
            region_code = "FR06"
        elif region == "Champagne-Ardenne":
            region_code = "FR07"
        elif region == "Franche-Comté":
            region_code = "FR09"
        elif region == "Haute-Normandie":
            region_code = "FR17"
        elif region == "Ile-de-France":
            region_code = "FR10"
        elif region == "Languedoc-Roussillon":
            region_code = "FR11"
        elif region == "Limousin":
            region_code = "FR12"
        elif region == "Lorraine":
            region_code = "FR13"
        elif region == "Midi-Pyrénées":
            region_code = "FR14"
        elif region == "Nord-Pas-de-Calais":
            region_code = "FR15"
        elif region == "Pays de la Loire":
            region_code = "FR18"
        elif region == "Picardie":
            region_code = "FR19"
        elif region == "Poitou-Charentes":
            region_code = "FR20"
        elif region == "PACA":
            region_code = "FR21"
        elif region == "Rhône-Alpes":
            region_code = "FR22"

        for keyword in keywords:
            uri = "/emploi-aeronautique/offres-emploi-aeronautique.php?search={0}&localisation={1}&contrat=1".format(keyword, region_code)
            soup = bs4.BeautifulSoup(toolbox.html_reader(webdomain,uri))
            for link in soup.find_all(href=re.compile("emploi-aeronautique")):
                pubtag = link.findNext("span", style='color: #777;')
                if pubtag is not None:
                    pubdate = pubtag.contents[0]
                    print(pubdate)
                    if pubdate is not None:
                        pubday = pubdate[0:2]
                        if pubday[0:1] == "0":
                            pubday = pubdate[1:2]
                        pubmonth = pubdate[3:5]
                        if pubmonth[0:1] == "0":
                            pubmonth = pubdate[4:5]
                        pubyear = pubdate[6:10]
                else:
                    pubdate = toolbox.current_date()

                link = link.get("href")
                if toolbox.compute_duration(pubdate) < daterange:
                    site_list.append("{0}".format(link))

        site_list = list(set(site_list))
        cleaned_site_list = []

        for element in site_list:
            if re.search('html$',element):
                cleaned_site_list.append(element)

        return cleaned_site_list

    def run_program(self, keywords, daterange, region):
        """Method to run program"""
        aerocontact_result = self._aerocontact_crawler(keywords, daterange, region)

        return aerocontact_result
