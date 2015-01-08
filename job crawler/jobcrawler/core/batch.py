# -*- coding: utf-8 -*-

###############################################
# Job Crawler - Batch program                 #
# Created by RIVES Yann                       #
# Crawl some website to find interesting jobs #
###############################################

### External modules importation ###

import os

### End of external modules importation ###

### Custom modules importation ###

from jobcrawler.core import core, toolbox

### End of custom modules importation ###

### Classes ###
class JobCrawlerBatch(object):

    def __init__(self):
        staticsxmlfile = "statics.xml"
        self.predefined_searches_dir = toolbox.xml_reader(staticsxmlfile, "profilespath")

    def _profile_reader(self, xml_file, entry):
        """Method to read datas from profile"""
        os.chdir(self.predefined_searches_dir)

        askedfield = toolbox.xml_reader(xml_file, entry)

        os.chdir("../.")

        return askedfield

    def run_program(self):
        """Method to run program Job crawler in batch mode"""
        print("Launching batch mode ...")

        search_profiles = os.listdir(self.predefined_searches_dir)

        for element in search_profiles:
            profile_name = element[0:-19]
            acc = self._profile_reader(element,"aerocontact")
            aefc = self._profile_reader(element,"aeroemploiformation")
            apecc = self._profile_reader(element,"apec")
            caoec = self._profile_reader(element,"caoemploi")
            ic = self._profile_reader(element,"indeed")
            mc = self._profile_reader(element,"monster")
            poc = self._profile_reader(element,"poleemploi")
            rjc = self._profile_reader(element,"regionjob")
            domain = self._profile_reader(element,"domain")
            keywords = tuple(self._profile_reader(element,"keywords").split(","))
            queries = tuple(self._profile_reader(element,"queries").split(","))
            region = self._profile_reader(element,"region")
            daterange = int(self._profile_reader(element,"daterange"))
            mailing_list = tuple(self._profile_reader(element,"mailinglist").split(","))

            runapp = core.JobCrawlerCore()
            runapp.run_program(profile_name=profile_name, acc=acc, aefc=aefc, apecc=apecc, caoec=caoec, ic=ic, mc=mc,\
                               poc=poc, rjc=rjc, domain=domain, keywords=keywords, queries=queries, region=region,\
                               daterange=daterange, mailing_list=mailing_list, db_management="True")

        print("Batch mode done")

### End of Classes ###

### Main program ###

if __name__=='__main__':
    runapp = JobCrawlerBatch()
    runapp.run_program()

### End of Main program ###
