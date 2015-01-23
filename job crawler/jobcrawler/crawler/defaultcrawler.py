'''
Created on 21 janv. 2015

@author: Guillaume
'''
from jobcrawler.core import toolbox

class defaultCrawler(object):
    def __init__(self, database, webdomain):
        self.database = database
        self.webdomain = webdomain
        
    def run(self):
        if not toolbox.ping_website(self.webdomain):
            raise toolbox.HTTPError("{0} not responding".format(self.webdomain))
        