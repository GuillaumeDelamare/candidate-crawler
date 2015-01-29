# -*- coding: utf-8 -*-

############################################
# Job Crawler - CAOemploi crawler          #
# Created by RIVES Yann                    #
# Crawl CAOemploi to find interesting jobs #
############################################

import re, bs4, logging
from jobcrawler.core import toolbox

logger = logging.getLogger("jobcrawler")

class CaoemploiCrawler(object):

    def _caoemploi_crawler(self, region):
        """Crawler for CAO emploi"""
        site_list = []
        webdomain = "www.cao-emplois.com"

        if not toolbox.ping_website(webdomain):
            logger.error("{0} not responding".format(webdomain))
            return

        if region == "Toute la France":
            region_code = "3d"
        elif region == "Alsace":
            region_code = "3dA"
        elif region == "Aquitaine":
            region_code = "3dB"
        elif region == "Auvergne":
            region_code = "3dC"
        elif region == "Basse-Normandie":
            region_code = "3dP"
        elif region == "Bourgogne":
            region_code = "3dD"
        elif region == "Bretagne":
            region_code = "3dE"
        elif region == "Centre":
            region_code = "3dF"
        elif region == "Champagne-Ardenne":
            region_code = "3dG"
        elif region == "Franche-Comté":
            region_code = "3dI"
        elif region == "Haute-Normandie":
            region_code = "3dQ"
        elif region == "Ile-de-France":
            region_code = "3dJ"
        elif region == "Languedoc-Roussillon":
            region_code = "3dK"
        elif region == "Limousin":
            region_code = "3dL"
        elif region == "Lorraine":
            region_code = "3dM"
        elif region == "Midi-Pyrénées":
            region_code = "3dN"
        elif region == "Nord-Pas-de-Calais":
            region_code = "3dO"
        elif region == "Pays de la Loire":
            region_code = "3dR"
        elif region == "Picardie":
            region_code = "3dS"
        elif region == "Poitou-Charentes":
            region_code = "3dT"
        elif region == "PACA":
            region_code = "3dU"
        elif region == "Rhône-Alpes":
            region_code = "3dV"

        uri = "/intl/jobseeker/jobs/jobresults.aspx?vt=full&excrit=st%3dA%3buse%3dALL%3bCID%3dFR%3bSID%{0}%3bTID%3d0%3bLOCCID%3dFR%3bENR%3dNO%3bDTP%3dDRNS%3bYDI%3dYES%3bIND%3dALL%3bPDQ%3dAll%3bPDQ%3dAll%3bPAYL%3d0%3bPAYH%3dGT120%3bPOY%3dNO%3bETD%3dALL%3bRE%3dALL%3bMGT%3dDC%3bSUP%3dDC%3bFRE%3d30%3bCHL%3dIL%3bQS%3dSID_UNKNOWN%3bSS%3dNO%3bTITL%3d0%3bOB%3d-relv%3bVT%3dtitle%3bRAD%3d30%3bJQT%3dRAD%3bJDV%3dFalse%3bHost%3dCE%3bSITEENT%3dCEJ%3bMaxLowExp%3d-1%3bRecsPerPage%3d50%3bSOFTID%3dCESOF13&sc=1".format(region_code)
        soup = bs4.BeautifulSoup(toolbox.html_reader(webdomain,uri))
        for link in soup.find_all(href=re.compile("jobdetails")):
            link = link.get("href")
            site_list.append("{0}".format(link))

        site_list = list(set(site_list))

        return site_list

    def run_program(self, region="Midi-Pyrénées"):
        """Method to run program"""
        logger.info("Crawling CAOemploi ...")

        caoemploi_result = self._caoemploi_crawler(region)

        logger.info("CAOemploi crawled")

        return caoemploi_result
