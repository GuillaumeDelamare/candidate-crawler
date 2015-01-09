'''
Created on 8 janv. 2015

@author: Pierre
'''

from scrapy.http import FormRequest
from scrapy.item import Item, Field
from scrapy.selector import Selector

from scrapy.spider import BaseSpider
from _cffi_backend import callback


class ApecItem(Item):
    urlCV = Field()
    print("bouh")


class CVSpider(BaseSpider):
    name = "CVFinder"
    allowed_domains = ["recruteurs.apec.fr"]
    start_urls = ['http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp?PEGA_HREF_950420318_0_0_doLogin=doLogin']
    
    
        
        

    def parse(self, response):
        
        formdata = {'PEGA_IMBT_12928340_0_0_doLogin':'47179308','PEGA_IMBT_24835201_0_0_doLogin':'6KPA43V8'}
        print("parse")
        yield FormRequest(url="http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp",
                                  method="POST",
                                  formdata=formdata,
                                  callback=self.parseB
                                  )

    def parseB(self,response):
        print("parseB")
        yield FormRequest(url="http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp?PEGA_HRSM_704371172_0_0_doGoConsulterCV=doGoConsulterCV"
                          ,method="POST",
                          callback=self.parseC)
        
    def parseC(self,response):
        print('parseC')#dans la methode suivante la partie entre HRSM_ et le premier _0 ne sert a rien et peut etre remplacee par n importe quoi
        yield FormRequest(url="http://recruteurs.apec.fr/CV/Candidapec/ApecCreateRequete.jsp?PEGA_HRSM_i<3consept_0_0_doSearchByCriteres=doSearchByCriteres"
                          ,method="POST"
                          ,formdata=self.formulaire
                          ,callback=self.parseD) #TODO rajouter les criteres
    
    def parseD(self,response):
        print("parseD")
        hxs = Selector(response)
        res = list()
        print(response)
        print(response)
        rows = hxs.xpath("//a[@id = 'unique-id']/@href")
        print(len(rows))
        print(len(rows))
        for row in rows:
            item = ApecItem()
            url = row.extract()
            item['urlCV'] = url
            print(url) 
            print(url)
            res = res.append(item)
        return res
        
    
    
    

   


    
    
    
    
    