# -*- coding: utf-8 -*-

###############################################
# Job Crawler - database management program   #
# Created by RIVES Yann                       #
# Crawl some website to find interesting jobs #
###############################################

import csv
from jobcrawler.core import toolbox
from datetime import datetime, date

def read_database(dbfile, usage="all"):
    """Read CSV database"""
    #TODO voir pour supprimer le usage
    csv_content = []
    
    read_database = csv.reader(open(dbfile,"rb"), delimiter=',')

    for line in read_database:
        if usage == "date":
            csv_content.append(line[0].strip("[]"))
        elif usage == "links":
            csv_content.append(line[1].strip("[]"))
        elif usage == "all":
            csv_content.append(line)

    return csv_content

def write_database(dbfile, linklist):
    """Write CSV database"""
    with open(dbfile,"ab") as csv_file:
        database = csv.writer(csv_file, delimiter=',')
        
        today = date.today().strftime("%d-%m-%Y")
        for link in linklist:
            database.writerow([today, link])
    
def clean_database(dbfile, max_store_day):
    """Clean CSV database"""
    cleaned_csv_content = [["DATE","LINK"]]
    
    # Read database
    csv_content = read_database(dbfile)
    csv_content.pop(0)

    # Filter on date
    fmt = "%d-%m-%Y"
    for element in csv_content:
        date = datetime.strptime(element[0], fmt).date()

        if toolbox.compute_duration(date) < max_store_day:
            cleaned_csv_content.append(element)

    with open(dbfile,"wb") as csv_file:
        database = csv.writer(csv_file, delimiter=',')
        database.writerows(cleaned_csv_content)
