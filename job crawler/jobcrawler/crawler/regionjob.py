# -*- coding: utf-8 -*-

############################################
# Job Crawler - Regionjob crawler          #
# Created by RIVES Yann                    #
# Crawl Regionjob to find interesting jobs #
############################################

### External modules importation ###

import re
import bs4

### End of external modules importation ###

### Custom modules importation ###

from jobcrawler.core import toolbox

### End of custom modules importation ###

### Classes ###
class RegionjobCrawler(object):
    def _regionjob_crawler_common(self, webdomain, domain, daterange):
        """Common part for crawler regions"""
        if not toolbox.ping_website(webdomain):
            print("{0} not responding".format(webdomain))
            return
        

        if domain == "Engineering":
            uri = "/offre_emploi/_Ingenierie---Mecanique-Aeron_Ingenierie---Mecanique-Aeron_0_14_0_0_2_0&page=1.aspx"
        elif domain == "Info-Hardware":
            uri = "/offre_emploi/_Informatique---Devel-Hardware_Informatique---Devel-Hardware_0_22_0_0_2_0.aspx"
        elif domain == "Info-Helpdesk":
            uri = "/offre_emploi/_SAV-Hotline-Teleconseiller_SAV-Hotline-Teleconseiller_0_35_0_0_2_0.aspx"
        elif domain == "Info-Software":
            uri = "/offre_emploi/_Informatique---Developpement_Informatique---Developpement_0_7_0_0_2_0.aspx"

        soup = bs4.BeautifulSoup(toolbox.html_reader(webdomain,uri))
        for link in soup.find_all(href=re.compile("offres_chartees")):
            pubtag = link.findPrevious("span", itemprop="datePosted")
            if pubtag is not None:
                pubdate = pubtag.contents[0]
                if pubdate is not None:
                    pubday = pubdate[0:2]
                    if pubday[0:1] == "0":
                        pubday = pubdate[1:2]
                    pubmonth = pubdate[3:5]
                    if pubmonth[0:1] == "0":
                        pubmonth = pubdate[4:5]
                    pubyear = 2014
            else:
                pubdate = toolbox.current_date()
                pubday = pubdate[0:2]
                if pubday[0:1] == "0":
                    pubday = pubdate[1:2]
                pubmonth = pubdate[3:5]
                if pubmonth[0:1] == "0":
                    pubmonth = pubdate[4:5]
                pubyear = pubdate[6:10]

            link = link.get("href")
            if toolbox.compute_duration(int(pubday),int(pubmonth),int(pubyear)) < daterange:
                self.site_list.append("http://{0}{1}".format(webdomain,link))
        

        self.site_list = list(set(self.site_list))

    def _crawl_all_regions(self, domain, daterange):
        """Crawler all regions"""
        website_liste = ("www.centrejob.com","www.nordjob.com","www.pacajob.com","www.rhonealpesjob.com",\
                         "www.sudouestjob.com","www.parisjob.com","www.ouestjob.com","www.estjob.com")

        for webdomain in website_liste:
            self._regionjob_crawler_common(webdomain, domain, daterange)

    def _regionjob_crawler(self, domain, daterange, region):
        """Crawler for Region job"""
        self.site_list = []

        if region == "Toute la France":
            self._crawl_all_regions(domain, daterange)
        elif region == "Auvergne" or region == "Centre" or region == "Limousin":
            self._regionjob_crawler_common("www.centrejob.com", domain, daterange)
        elif region == "Haute-Normandie" or region == "Nord-Pas-de-Calais" or region == "Picardie":
            self._regionjob_crawler_common("www.nordjob.com", domain, daterange)
        elif region == "Languedoc-Roussillon" or region == "PACA":
            self._regionjob_crawler_common("www.pacajob.com", domain, daterange)
        elif region == "Rhône-Alpes":
            self._regionjob_crawler_common("www.rhonealpesjob.com", domain, daterange)
        elif region == "Aquitaine" or region == "Midi-Pyrénées":
            self._regionjob_crawler_common("www.sudouestjob.com", domain, daterange)
        elif region == "Ile-de-France":
            self._regionjob_crawler_common("www.parisjob.com", domain, daterange)
        elif region == "Basse-Normandie" or region == "Bretagne" or region == "Pays de la Loire" or region == "Poitou-Charentes":
            self._regionjob_crawler_common("www.ouestjob.com", domain, daterange)
        elif region == "Alsace" or region == "Bourgogne" or region == "Champagne-Ardenne" or region == "Franche-Comté" or region == "Lorraine":
            self._regionjob_crawler_common("www.estjob.com", domain, daterange)

        return self.site_list

    def run_program(self, domain="Engineering", daterange=3, region="Midi-Pyrénées"):
        """Method to run program"""
        print("Crawling Regionjob ...")

        regionjob_result = self._regionjob_crawler(domain, daterange, region)

        print("Regionjob crawled")

        return regionjob_result

### End of Classes ###

### Main program ###

if __name__=='__main__':
    runapp = RegionjobCrawler()
    print(runapp.run_program())

### End of Main program ###
