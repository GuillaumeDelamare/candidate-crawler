'''
Created on 8 janv. 2015

@author: Pierre
'''

from scrapy.http import FormRequest,Request
from scrapy.item import Item, Field
from scrapy.selector import Selector
from scrapy.contrib.spiders.init import InitSpider
from scrapy.spider import BaseSpider
from _cffi_backend import callback
from twisted.python.formmethod import Password
from time import sleep


class ApecItem(Item):
    urlCV = Field()
    print("bouh")


class CVSpider(InitSpider):
    name = "CVFinder"
    allowed_domains = ["recruteurs.apec.fr"]
    start_urls = ['http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp?PEGA_HREF_950420318_0_0_doLogin=doLogin']
    password = ""
    login = ""
    critere = {}
    login_page = 'http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp?PEGA_HREF_950420318_0_0_doLogin=doLogin'
    
    def start_requests(self):
        yield FormRequest(
                      url="http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp?PEGA_HRSM_704371172_0_0_doGoConsulterCV=doGoConsulterCV",
                      formdata={'session_key': self.login, 'session_password': self.password},
                      callback=self.check_login_response,
                      dont_filter=True
    )
    
    
    def __init__(self, login, password, critere):
        self.critere = critere
        self.login = login
        self.password = password 
        
    def login(self, response):
    #"""Generate a login request."""
        return FormRequest.from_response(response,
            formdata={'session_key': self.login, 'session_password': self.password},
            callback=self.check_login_response)

    def check_login_response(self, response):
    #"""Check the response returned by a login request to see if we aresuccessfully logged in."""
        if "Sign Out" in response.body:
            self.log("\n\n\nSuccessfully logged in. Let's start crawling!\n\n\n")
        # Now the crawling can begin..
            self.log('Hi, this is an item page! %s' % response.url)

            return 

        else:
            self.log("\n\n\nFailed, Bad times :(\n\n\n")
        # Something went wrong, we couldn't log in, so nothing happens.


#     def parse(self, response):
#          
#         formdata = {'PEGA_IMBT_12928340_0_0_doLogin':self.login,'PEGA_IMBT_24835201_0_0_doLogin':self.password}
#         print("parse")
#         yield FormRequest(url="http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp?PEGA_HREF_379848439_0_0_doLogin=doLogin",
#                                   formdata=formdata,
#                                   callback=self.parseB
#                                   )
#         

    def parseB(self,response):
        print("parseB")
        yield FormRequest(url="http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp?PEGA_HRSM_704371172_0_0_doGoConsulterCV=doGoConsulterCV"
                          ,method="POST",
                          callback=self.parseC)
    
        
    def parseC(self,response):
        print('parseC')#dans la methode suivante la partie entre HRSM_ et le premier _0 ne sert a rien et peut etre remplacee par n importe quoi
        yield FormRequest(url="http://recruteurs.apec.fr/CV/Candidapec/ApecCreateRequete.jsp?PEGA_HRSM_i<3consept_0_0_doSearchByCriteres=doSearchByCriteres"
                          ,method="POST"
                          #,formdata=self.formulaire
                          #formdata = {'PEGA_TXFD_109774019_0_keywords':'catia' ,}
                          ,callback=self.parseD) #TODO rajouter les criteres
     
    
    def parseD(self,response):
        print("parseD")
        hxs = Selector(response)
        res = list()
        print(response)
        print(response)
        rows = hxs.xpath("//div[@id='chenillard']")
        print(rows[0])
        print(len(rows))
        for row in rows:
            item = ApecItem()
            url = row.extract()
            item['urlCV'] = url
            print(url) 
            print(url)
            res = res.append(item)
        return res
        
    
    
    

   


    
    
    
    
    