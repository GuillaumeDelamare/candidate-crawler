# -*- coding: utf-8 -*-

#######################################
# Job Crawler - Apec crawler          #
# Created by RIVES Yann               #
# Crawl Apec to find interesting jobs #
#######################################

### External modules importation ###

import re
import bs4

### End of external modules importation ###

### Custom modules importation ###

from jobcrawler.core import toolbox

### End of custom modules importation ###

### Classes ###
class ApecCrawler(object):

    def _apec_crawler(self, keywords, daterange, region):
        """Crawler for APEC"""
        site_list = []
        webdomain = "cadres.apec.fr"

        if not toolbox.ping_website(webdomain):
            print("{0} not responding".format(webdomain))
            return

        if region == "Toute la France":
            region_code = ""
        elif region == "Alsace":
            region_code = "&region=700"
        elif region == "Aquitaine":
            region_code = "&region=701"
        elif region == "Auvergne":
            region_code = "&region=702"
        elif region == "Basse-Normandie":
            region_code = "&region=703"
        elif region == "Bourgogne":
            region_code = "&region=704"
        elif region == "Bretagne":
            region_code = "&region=705"
        elif region == "Centre":
            region_code = "&region=706"
        elif region == "Champagne-Ardenne":
            region_code = "&region=707"
        elif region == "Franche-Comté":
            region_code = "&region=709"
        elif region == "Haute-Normandie":
            region_code = "&region=710"
        elif region == "Ile-de-France":
            region_code = "&region=711"
        elif region == "Languedoc-Roussillon":
            region_code = "&region=712"
        elif region == "Limousin":
            region_code = "&region=713"
        elif region == "Lorraine":
            region_code = "&region=714"
        elif region == "Midi-Pyrénées":
            region_code = "&region=715"
        elif region == "Nord-Pas-de-Calais":
            region_code = "&region=716"
        elif region == "Pays de la Loire":
            region_code = "&region=717"
        elif region == "Picardie":
            region_code = "&region=718"
        elif region == "Poitou-Charentes":
            region_code = "&region=719"
        elif region == "PACA":
            region_code = "&region=720"
        elif region == "Rhône-Alpes":
            region_code = "&region=721"

        for keyword in keywords:
            uri = "/MesOffres/RechercheOffres/ApecRechercheOffre.jsp?keywords={0}{1}".format(keyword, region_code)
            soup = bs4.BeautifulSoup(toolbox.html_reader(webdomain,uri))
            for link in soup.find_all(href=re.compile("offre-d-emploi-")):
                pubtag = link.findNext("strong")
                if pubtag is not None:
                    pubdate = pubtag.contents[0]
                    if pubdate[0:5] == "Parue":
                        pubday = pubdate[9:11]
                        if pubday[0:1] == "0":
                            pubday = pubdate[10:11]
                        pubmonth = pubdate[12:14]
                        if pubmonth[0:1] == "0":
                            pubmonth = pubdate[13:14]
                        pubyear = "20{0}".format(pubdate[15:17])
                    else:
                        pubdate = toolbox.current_date()
                        pubday = pubdate[0:2]
                        if pubday[0:1] == "0":
                            pubday = pubdate[1:2]
                        pubmonth = pubdate[3:5]
                        if pubmonth[0:1] == "0":
                            pubmonth = pubdate[4:5]
                        pubyear = pubdate[6:10]
                else:
                    pubdate = toolbox.current_date()
                    pubday = pubdate[0:2]
                    if pubday[0:1] == "0":
                        pubday = pubdate[1:2]
                    pubmonth = pubdate[3:5]
                    if pubmonth[0:1] == "0":
                        pubmonth = pubdate[4:5]
                    pubyear = pubdate[6:10]

                link = re.sub(("\?(.*?)$"),'',link.get("href"))
                if toolbox.compute_duration(int(pubday),int(pubmonth),int(pubyear)) < daterange:
                    site_list.append("http://{0}{1}".format(webdomain,link))

        site_list = list(set(site_list))

        return site_list

    def run_program(self,keywords=("dessinateur","catia"), daterange=3, region="Midi-Pyrénées"):
        """Method to run program"""
        print("Crawling Apec ...")

        apec_result = self._apec_crawler(keywords, daterange, region)

        print("Apec crawled")

        return apec_result

### End of Classes ###

### Main program ###

if __name__=='__main__':
    runapp = ApecCrawler()
    print(runapp.run_program())

### End of Main program ###
