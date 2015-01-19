'''
Created on 7 janv. 2015

@author: Jonathan
'''
### External modules importation ###

import os
import datetime
import httplib
from xml.etree import ElementTree
from ConfigParser import ConfigParser

### End of external modules importation ###

### Functions ###

def current_date():
    """Get current date, and format it"""
    currentdate = datetime.date.today().strftime("%d-%m-%Y") # We get current date and format it DD-MM-YYYY

    return currentdate

def compute_duration(day,month,year):
    """Compute duration between 2 dates"""
    duration = datetime.datetime.now() - datetime.datetime(year,month,day)

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


def xml_reader(input_file, entry):
    """Read datas from an XML file"""
    xmlfile = open(input_file, "r")
    tree = ElementTree.ElementTree()
    tree.parse(xmlfile)
    root = tree.getroot()

    askedfield = root.find(entry).text

    xmlfile.close()

    return askedfield

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

def xml_writer(input_file, output_file, entry_value_dict, backup=True):
    """Write datas to an XML file"""
    xmlfile = open(input_file, "r")
    tree = ElementTree.ElementTree()
    tree.parse(xmlfile)
    root = tree.getroot()

    for key, value in entry_value_dict.items():
        root.find(key).text = value

    tree.write(output_file, encoding="utf-8", xml_declaration=True)
    xmlfile.close()

    if backup:
        os.remove(input_file)
        os.rename(output_file,input_file)

def get_apec_id():
    """Recupere le login et le password dans le fichier config.init permmetant d'acceder au site de l'APEC
    """
    config = ConfigParser('./config.ini')
    login = config.get('APEC','login')
    password = config.get('APEC','password')
    return login, password

def getconfigvalue(section, option):
    config = ConfigParser()
    config.read("./config.ini")

    return config.get(section, option)

def writeconfigvalue(section, option, value):
    config = ConfigParser()
    config.read("./config.ini")

    config.set(section, option, u''.join(unicode(value)).encode('utf-8'))
    with open("./config.ini", 'wb') as configfile:
        config.write(configfile)
    
### End of functions ###