# -*- coding: utf-8 -*-

###############################################
# Job Crawler - profiles management program   #
# Created by RIVES Yann                       #
# Crawl some website to find interesting jobs #
###############################################

### External modules importation ###

import os
import shutil

### End of external modules importation ###

from jobcrawler.core import toolbox

### Custom modules importation ###

### End of custom modules importation ###

### Functions ###

def create_profile(profiles="Azel", acs=True, aefs=True, apecs=True, caoes=True, ids=True,ms=True, pos=True, rjs=True,\
                   domains="Engineering", keywordss=("dessinateur"), queriess=("catia"),\
                   regions="Midi-Pyrénées", dateranges=3, mls=""):
    """Create search profile"""
    profile_template = "profile_template.xml"
    staticsxmlfile = "statics.xml"
    profilepath = toolbox.xml_reader(staticsxmlfile, "profilespath")
    profile_name = "{0}-{1}.xml".format(profiles,toolbox.timestamp())

    write_dict = {}
    write_dict["name"] = profiles
    write_dict["aerocontact"] = str(acs)
    write_dict["aeroemploiformation"] = str(aefs)
    write_dict["apec"] = str(apecs)
    write_dict["caoemploi"] = str(caoes)
    write_dict["indeed"] = str(ids)
    write_dict["monster"] = str(ms)
    write_dict["poleemploi"] = str(pos)
    write_dict["regionjob"] = str(rjs)
    write_dict["domain"] = domains
    write_dict["keywords"] = str(keywordss)
    write_dict["queries"] = str(queriess)
    write_dict["region"] = regions
    write_dict["daterange"] = str(dateranges)
    write_dict["mailinglist"] = str(mls)

    toolbox.xml_writer(profile_template, profile_name, write_dict, backup=False)

    shutil.move(profile_name, profilepath)

    return profile_name

def delete_profile(name):
    """Delete search profile"""
    print ("Delete {0}".format(name))

    staticsxmlfile = "statics.xml"
    profilepath = toolbox.xml_reader(staticsxmlfile, "profilespath")

    os.remove("{0}/{1}".format(profilepath, name))

def edit_profile(name, acc, aefc, apecc, caoec, idc,mc, poc, rjc,\
                 domain, keywords, queries, region, daterange, ml):
    """Edit search profile"""
    print ("Write {0}".format(name))

    staticsxmlfile = "statics.xml"
    profilepath = toolbox.xml_reader(staticsxmlfile, "profilespath")

    os.chdir(profilepath)

    profile_name = name
    profile_temp = "{0}-sav".format(name)

    write_dict = {}
    write_dict["aerocontact"] = str(acc)
    write_dict["aeroemploiformation"] = str(aefc)
    write_dict["apec"] = str(apecc)
    write_dict["caoemploi"] = str(caoec)
    write_dict["indeed"] = str(idc)
    write_dict["monster"] = str(mc)
    write_dict["poleemploi"] = str(poc)
    write_dict["regionjob"] = str(rjc)
    write_dict["domain"] = domain
    write_dict["keywords"] = str(keywords)
    write_dict["queries"] = str(queries)
    write_dict["region"] = region
    write_dict["daterange"] = str(daterange)
    write_dict["mailinglist"] = str(ml)

    toolbox.xml_writer(profile_name, profile_temp, write_dict, backup=True)

    os.chdir("../.")


### End of Functions ###
if __name__=='__main__':
    create_profile()