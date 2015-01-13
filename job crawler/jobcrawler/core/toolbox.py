# -*- coding: utf-8 -*-

##############################
# Job crawler toolbox        #
# Created by RIVES Yann      #
# Some tools for job crawler #
##############################

### External modules importation ###

import os
import datetime
import httplib
import xml.etree.ElementTree
import ConfigParser

### End of external modules importation ###

### Functions ###

def timestamp():
    """Create a unique time stamp"""
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S") # We get current date and format it YYYYMMDDHHMMSS

    return now

def current_date():
    """Get current date, and format it"""
    currentdate = datetime.date.today().strftime("%d-%m-%Y") # We get current date and format it DD-MM-YYYY

    return currentdate

def compute_duration(date):
    """Compute duration between 2 dates"""
    duration = datetime.datetime.now() - datetime.datetime(date)

    return duration.days

def ping_website(url):
    """Ping a website"""
    website_status = True

    try:
        conn = httplib.HTTPConnection(url)
        conn.request("GET",url)
    except:
        website_status = False

    return website_status

def html_reader(domainName,uri):
    """Read an HTML page"""
    conn = httplib.HTTPConnection(domainName)
    conn.request("GET",uri)
    r1 = conn.getresponse()

    if r1.reason != "OK":
        print("{0} - {1}".format(r1.status, r1.reason))
        print(r1.getheader('Location'))

    htmlpage = r1.read()

    return htmlpage

def xml_reader(input_file, entry):
    """Read datas from an XML file"""
    xmlfile = open(input_file, "r")
    tree = xml.etree.ElementTree.ElementTree()
    tree.parse(xmlfile)
    root = tree.getroot()

    askedfield = root.find(entry).text

    xmlfile.close()

    return askedfield

def xml_writer(input_file, output_file, entry_value_dict, backup=True):
    """Write datas to an XML file"""
    xmlfile = open(input_file, "r")
    tree = xml.etree.ElementTree.ElementTree()
    tree.parse(xmlfile)
    root = tree.getroot()

    for key, value in entry_value_dict.items():
        root.find(key).text = value

    tree.write(output_file, encoding="utf-8", xml_declaration=True)
    xmlfile.close()

    if backup:
        os.remove(input_file)
        os.rename(output_file,input_file)

def getconfigvalue(section, option):
    config = ConfigParser.ConfigParser()
    config.read("./config.ini")

    return config.get(section, option)

def writeconfigvalue(section, option, value):
    config = ConfigParser.ConfigParser()
    config.read("./config.ini")

    config.set(section, option, u''.join(unicode(value)).encode('utf-8'))
    with open("./config.ini", 'wb') as configfile:
        config.write(configfile)
    

