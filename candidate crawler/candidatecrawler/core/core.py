'''
Created on 7 janv. 2015

@author: Jonathan
'''

### External modules importation ###


### End of external modules importation ###

### Custom modules importation ###


### End of custom modules importation ###

### Classes ###
class CandidateCrawlerCore(object):
    #TODO: Listeners
    keyword = ""
    region = []
    mobilite = ""
    salaire = ""
    disponibilite = ""
    fraicheur = ""
    nombreCV = 50 
    
    
    def __init__(self,keyword,region,mobilite,salaire,disponibilite,fraicheur,nombreCV):
        """Initialisation du spider"""
        
        self.keyword = keyword 
        self.region = region
        self.mobilite = mobilite
        self.salaire = salaire
        self.disponibilite = disponibilite
        self.fraicheur = fraicheur
        self.nombreCV = nombreCV
         
    
    
    
#     #TODO: Appel crawler
#     def crawl(self,):
#     
#     #TODO: Telechargement des CVs
#     
#     
#     #TODO: Creation de l'excel
# 
# 
#     #TODO: Zippage



    