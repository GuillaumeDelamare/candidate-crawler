# -*- coding: utf-8 -*-

##############################
# Job crawler toolbox        #
# Created by RIVES Yann      #
# Some tools for job crawler #
##############################

### External modules importation ###

import datetime
import httplib
import ConfigParser

### End of external modules importation ###

### Functions ###

def timestamp():
    """Create a unique time stamp"""
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S") # We get current date and format it YYYYMMDDHHMMSS

    return now

def compute_duration(date):
    """Compute duration between 2 dates"""
    duration = datetime.date.today() - date

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

def getconfigvalue(section, option):
    config = ConfigParser.ConfigParser()
    config.read("./config.ini")

    return config.get(section, option).decode("utf-8")

def writeconfigvalue(section, option, value):
    config = ConfigParser.ConfigParser()
    config.read("./config.ini")

    config.set(section, option, unicode(value).encode('utf-8'))
    with open("./config.ini", 'wb') as configfile:
        config.write(configfile)
    