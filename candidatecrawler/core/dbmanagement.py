'''
Created on 7 janv. 2015

@author: Jonathan
'''
### External modules importation ###

import os
import shutil
import csv

### End of external modules importation ###

### Custom modules importation ###

from candidatecrawler.core import toolbox

### End of custom modules importation ###

### Functions ###

def read_database(dbfile, usage):
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
    csv_file = open(dbfile,"a",newline='')

    write_database = csv.writer(csv_file, delimiter=',')

    for line in linklist:
        write_database.writerow([toolbox.current_date(),line])

    csv_file.close()

def clean_database(dbfile, max_store_day):
    """Clean CSV database"""
    csv_content = []
    cleaned_csv_content = [["DATE","LINK"]]

    if os.path.isfile("{0}.backup".format(dbfile[0:-4])):
        os.remove("{0}.backup".format(dbfile[0:-4]))
        shutil.copy(dbfile,"{0}.backup".format(dbfile[0:-4]))
    else:
        shutil.copy(dbfile,"{0}.backup".format(dbfile[0:-4]))

    read_database = csv.reader(open(dbfile,"r"), delimiter=',')

    for line in read_database:
        csv_content.append(line)

    csv_content.pop(0)

    for element in csv_content:
        date = element[0]
        linkday = date[0:2]
        if linkday[0:1] == "0":
            linkday = date[1:2]
        linkmonth = date[3:5]
        if linkmonth[0:1] == "0":
            linkmonth = date[4:5]
        linkyear = date[6:10]

        if toolbox.compute_duration(int(linkday),int(linkmonth),int(linkyear)) < max_store_day:
            cleaned_csv_content.append(element)

    csv_file = open(dbfile,"w",newline='')
    write_database = csv.writer(csv_file, delimiter=',')

    for line in cleaned_csv_content:
        write_database.writerow([line[0],line[1]])

    csv_file.close()

### End of Functions ###