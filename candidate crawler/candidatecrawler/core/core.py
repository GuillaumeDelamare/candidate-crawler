'''
Created on 7 janv. 2015

@author: Jonathan
'''

### External modules importation ###

import re
import urllib
import bs4

### End of external modules importation ###

### Custom modules importation ###

from candidatecrawler.core import toolbox, dbmanagement
from candidatecrawler.crawler import poleemploi


### End of custom modules importation ###

### Classes ###
class CandidateCrawlerCore(object):

    def _values_initializer(self):
        """Method to initialize variables"""
        self.configxmlfile = "Config.xml"
        self.dbfile = toolbox.xml_reader(self.configxmlfile, "dbfile").replace("\\","\\")      
        self.newlinks_list = []
        self.final_links_list = []

        self.max_store_day = 40  #TODO a voir, fraicheur = critère ? 

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

#     def run_program(self, profile_name="", acc="True", aefc="True", apecc="True", caoec="True", ic="True", mc="True", poc="True",\
#                     rjc="True", domain="Engineering", keywords=("dessinateur","catia"), queries=("catia","meca"), region="Midi-Pyrénées",\
#                     daterange=3, mailing_list=("",), db_management = "False"):
#         """Method to run program"""
#         print("Launching core program")
# 
#         self._values_initializer()

       
    def findCandidate(self, keywords, region,db_management = False):
        runpoc = poleemploi.PoleemploiCrawler()
        for link in runpoc.run_program(keywords=("dessinateur","catia"),region):
            self.newlinks_list.append(link)
            self._links_management(self.newlinks_list)

        if db_management == True:
            dbmanagement.write_database(self.dbfile, self.final_links_list)
            dbmanagement.clean_database(self.dbfile, self.max_store_day)
            
        #TODO télécharger les cv, faire le excel et zip!
        print("{0} new candidates found".format(len(self.final_links_list)))
        print("Done\n")

        return self.final_links_list #return le zip

### End of Classes ###

### Main program ###

if __name__=='__main__':
    runapp = CandidateCrawlerCore()
    runapp.run_program()

### End of Main program ###