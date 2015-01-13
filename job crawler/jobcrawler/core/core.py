# -*- coding: utf-8 -*-

###############################################
# Job Crawler - Core program                  #
# Created by RIVES Yann                       #
# Crawl some website to find interesting jobs #
###############################################

### External modules importation ###

import re
import urllib
import bs4

### End of external modules importation ###

### Custom modules importation ###

from jobcrawler.core import dbmanagement, toolbox, myEmail
from jobcrawler.crawler import aerocontact, aeroemploiformation, apec, caoemploi, indeed, monster, poleemploi, regionjob

### End of custom modules importation ###

### Classes ###
class JobCrawlerCore(object):

    def _values_initializer(self):
        """Method to initialize variables"""
        self.configxmlfile = "Config.xml"
        self.dbfile = toolbox.xml_reader(self.configxmlfile, "dbfile").replace("\\","\\")
        self.exclude_list = tuple(toolbox.xml_reader(self.configxmlfile, "excludes").split(','))

        self.newlinks_list = []
        self.final_links_list = []

        self.max_store_day = 40

    def _links_management(self, linklist, queries):
        """Method to manage links in global list"""
        sorted_links_list = []

        linklist = list(set(linklist))

        for link in linklist:
            if link not in dbmanagement.read_database(self.dbfile, "links"):
                sorted_links_list.append(link)

        for link in sorted_links_list:
            error_code = False

            try:
                htmlpage = urllib.urlopen(link).read()
                soup = bs4.BeautifulSoup(htmlpage)

                if self.exclude_list[0] != "":
                    for word in self.exclude_list:
                        if str(soup.body.find_all(text=re.compile(word, re.IGNORECASE))) != "[]" and not "cao-emploi" in link:
                            error_code = True

                if queries[0] != "":
                    criteria_found = False
                    for word in queries:
                        if str(soup.body.find_all(text=re.compile(word, re.IGNORECASE))) != "[]":
                            criteria_found = True

                    if not criteria_found:
                        error_code = True

            except:
                error_code = True
                print("Error on link {0}".format(link))

            if not error_code:
                self.final_links_list.append(link)

        self.final_links_list = list(set(self.final_links_list))

    def run_program(self, profile_name="", acc="True", aefc="True", apecc="True", caoec="True", ic="True", mc="True", poc="True",\
                    rjc="True", domain="Engineering", keywords=("dessinateur","catia"), queries=("catia","meca"), region="Midi-Pyrénées",\
                    daterange=3, mailing_list=("",), db_management = "False"):
        """Method to run program"""
        print("Launching core program")

        self._values_initializer()

        if acc == "True":
            runacc = aerocontact.AerocontactCrawler()
            for link in runacc.run_program(keywords,daterange,region):
                self.newlinks_list.append(link)
        if aefc == "True":
            runaefc = aeroemploiformation.AeroemploiformationCrawler()
            for link in runaefc.run_program(domain,region):
                self.newlinks_list.append(link)
        if apecc == "True":
            runapecc = apec.ApecCrawler()
            for link in runapecc.run_program(keywords,daterange,region):
                self.newlinks_list.append(link)
        if caoec == "True":
            runcaoec = caoemploi.CaoemploiCrawler()
            for link in runcaoec.run_program(region):
                self.newlinks_list.append(link)
        if ic == "True":
            runic = indeed.IndeedCrawler()
            for link in runic.run_program(keywords,daterange,region):
                self.newlinks_list.append(link)
        if mc == "True":
            runmc = monster.MonsterCrawler()
            for link in runmc.run_program(keywords,daterange,region):
                self.newlinks_list.append(link)
        if poc == "True":
            runpoc = poleemploi.PoleemploiCrawler()
            for link in runpoc.run_program(keywords,daterange,region):
                self.newlinks_list.append(link)
        if rjc == "True":
            runrjc = regionjob.RegionjobCrawler()
            for link in runrjc.run_program(domain,daterange,region):
                self.newlinks_list.append(link)

        self._links_management(self.newlinks_list, queries)

        if db_management == "True":
            dbmanagement.write_database(self.dbfile, self.final_links_list)
            dbmanagement.clean_database(self.dbfile, self.max_store_day)

        if mailing_list[0] != "":
            runmail = myEmail.JobCrawlerEmail()
            runmail.run_program(profile_name, mailing_list, self.final_links_list)

        print("{0} new jobs found".format(len(self.final_links_list)))
        print("Done\n")

        return self.final_links_list

### End of Classes ###

### Main program ###

if __name__=='__main__':
    runapp = JobCrawlerCore()
    runapp.run_program()

### End of Main program ###
