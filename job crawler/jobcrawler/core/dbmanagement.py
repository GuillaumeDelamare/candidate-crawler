# -*- coding: utf-8 -*-

###############################################
# Job Crawler - database management program   #
# Created by RIVES Yann                       #
# Crawl some website to find interesting jobs #
###############################################

import csv
from datetime import datetime

class dbheader:
    FOUNDDATE = "DATE"
    LINK = "LIEN"
    FIRM = "ENTREPRISE"
    RELEASEDATE = "DATE DE PUBLICATION"
    SEARCHKEYWORDS = "MOTS CLE DE RECHERCHE"
    FILTERKEYWORDS = "MOTS CLE DE FILTRAGE"
    TITLE = "TITRE"



class ad(object):
    def __init__(self, link, founddate=None, releasedate=None, searchkeywords=[], filterkeywords=[], firm=None, title=None):
        self.link = link
        self.founddate = founddate
        self.releasedate = releasedate
        self.searchkeywords = searchkeywords
        self.filterkeywords = filterkeywords
        self.firm = firm
        self.title = title
    
    def __str__(self, *args, **kwargs):
        s = "[{}, {}, {}, {}, {}, {}]"
        s = s.format(self.link, self.founddate, self.releasedate, self.searchkeywords, \
                     self.filterkeywords, self.firm)
        return s
    
    def __eq__(self, o):
        if isinstance(o, ad):
            return self.link == o.link
    
        return False
    
    def __ne__(self, o):
        return not self == o
    
    def merge(self, o):
        if not isinstance(o, ad):
            raise TypeError("o must be an ad type")
        
        if self.founddate is None:
            self.founddate = o.founddate
        
        if self.releasedate is None:
            self.releasedate = o.releasedate
        
        if self.firm is None:
            self.firm = o.firm
        
        self.filterkeywords.extend(o.filterkeywords)
        self.filterkeywords = list(set(self.filterkeywords))
        self.searchkeywords.extend(o.searchkeywords)
        self.searchkeywords = list(set(self.searchkeywords))



class database(object):
    datefmt = "%Y-%m-%d"
    
    def __init__(self, path):
        self.path = path
        self.ads = []
        
        try:
            self.read()
        except:
            pass
    
    def __str__(self, *args, **kwargs):
        return '\n'.join(map(str, self.ads))
    
    def read(self):
        with open(self.path, 'rb') as f:
            reader = csv.DictReader(f, dialect='excel', delimiter=';')
            for row in reader:
                try:
                    foundate = datetime.strptime(row[dbheader.FOUNDDATE], self.datefmt)
                except ValueError:
                    foundate = None
                
                try:
                    releasedate = datetime.strptime(row[dbheader.RELEASEDATE], self.datefmt)
                except ValueError:
                    releasedate = None
                
                if row[dbheader.SEARCHKEYWORDS] == "":
                    searchkeywords = []
                else:
                    searchkeywords = row[dbheader.SEARCHKEYWORDS].split(',')
                
                if row[dbheader.FILTERKEYWORDS] == "":
                    filterkeywords = []
                else:
                    filterkeywords = row[dbheader.FILTERKEYWORDS].split(',')
                
                if row[dbheader.FIRM] == "None":
                    firm = None
                else:
                    firm = row[dbheader.FIRM]
                    
                if row[dbheader.TITLE] == "None":
                    title = None
                else:
                    title = row[dbheader.TITLE]
                
                self.ads.append(ad(row[dbheader.LINK],
                                   foundate,
                                   releasedate,
                                   searchkeywords,
                                   filterkeywords,
                                   firm,
                                   title))
    
    def write(self):
        fieldnames = [dbheader.FOUNDDATE,
                      dbheader.TITLE,
                      dbheader.FIRM,
                      dbheader.RELEASEDATE,
                      dbheader.SEARCHKEYWORDS,
                      dbheader.FILTERKEYWORDS,
                      dbheader.LINK]
        
        with open(self.path, 'wb') as csvfile:
            writer = csv.DictWriter(csvfile, dialect='excel', fieldnames=fieldnames, delimiter=';')
        
            writer.writeheader()
            for ad in self.ads:
                try:
                    foundate = ad.founddate.strftime(self.datefmt)
                except AttributeError:
                    foundate = ""
                
                try:
                    releasedate = ad.releasedate.strftime(self.datefmt)
                except AttributeError:
                    releasedate = ""
                
                searchkeywords = ",".join(ad.searchkeywords)
                
                filterkeywords = ",".join(ad.filterkeywords)
                
                writer.writerow({dbheader.FOUNDDATE: foundate,
                                 dbheader.TITLE: ad.title,
                                 dbheader.FIRM: ad.firm,
                                 dbheader.RELEASEDATE: releasedate,
                                 dbheader.SEARCHKEYWORDS: searchkeywords,
                                 dbheader.FILTERKEYWORDS: filterkeywords,
                                 dbheader.LINK: ad.link})
    
    def merge(self):
        temp = self.ads
        self.ads = []
        
        for ad in temp:
            if ad in self.ads:
                self.ads[self.ads.index(ad)].merge(ad)
            else:
                self.ads.append(ad)
    