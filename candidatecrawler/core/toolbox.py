'''
Created on 7 janv. 2015

@author: Julie S
'''
from xml.etree import ElementTree

def xml_reader(input_file, entry):
    """Read datas from an XML file"""
    xmlfile = open(input_file, "r", encoding="utf-8")
    tree = ElementTree.ElementTree()
    tree.parse(xmlfile)
    root = tree.getroot()

    askedfield = root.find(entry).text

    xmlfile.close()

    return askedfield

