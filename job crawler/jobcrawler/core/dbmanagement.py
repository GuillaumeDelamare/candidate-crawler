# -*- coding: utf-8 -*-

###############################################
# Job Crawler - database management program   #
# Created by RIVES Yann                       #
# Crawl some website to find interesting jobs #
###############################################

### External modules importation ###

import os
import shutil
import csv

### End of external modules importation ###

### Custom modules importation ###

from jobcrawler.core import toolbox

### End of custom modules importation ###

### Functions ###

def read_database(dbfile, usage="all"):
    """Read CSV database"""
    csv_content = []
    read_database = csv.reader(open(dbfile,"r"), delimiter=',')

    for line in read_database:
        if usage == "date":
            csv_content.append(str(line[0]).strip("[]"))
        elif usage == "links":
            csv_content.append(str(line[1]).strip("[]"))
        elif usage == "all":
            csv_content.append(str(line).replace("[]"))

    return csv_content

def write_database(dbfile, linklist):
    """Write CSV database"""
    csv_file = open(dbfile,"a")

    write_database = csv.writer(csv_file, delimiter=',')

    for line in linklist:
        write_database.writerow([toolbox.current_date(),line])

    csv_file.close()

def clean_database(dbfile, max_store_day):
    """Clean CSV database"""
    cleaned_csv_content = [["DATE","LINK"]]
    
    # Create a backup
    backupfile = "{0}.backup".format(dbfile[0:-4])
    if os.path.isfile(backupfile):
        os.remove(backupfile)
    shutil.copy(dbfile,backupfile)
    
    # Read database
    csv_content = read_database(dbfile)
    csv_content.pop(0)

    # Filter on date
    fmt = "%d-%m-%Y"
    for element in csv_content:
        date = datetime.strptime(element[0], fmt)

        if toolbox.compute_duration(date) < max_store_day:
            cleaned_csv_content.append(element)

    csv_file = open(dbfile,"w")
    write_database = csv.writer(csv_file, delimiter=',')

    for line in cleaned_csv_content:
        write_database.writerow([line[0],line[1]])

    csv_file.close()

### End of Functions ###
