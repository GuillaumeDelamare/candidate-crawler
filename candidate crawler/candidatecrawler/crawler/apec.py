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


class LogSpider(BaseSpider):
    name = "CVFinder"
    allowed_domains = ["recruteurs.apec.fr"]
    start_urls = ['http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp?PEGA_HREF_950420318_0_0_doLogin=doLogin']


    def parse(self, response):
        
        formdata = {'PEGA_IMBT_12928340_0_0_doLogin':'47179308','PEGA_IMBT_24835201_0_0_doLogin':'6KPA43V8'}
        print("tata")
        yield FormRequest(url="http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp",
                                  method="POST",
                                  formdata=formdata,
                                  callback=ClickSpider.parse,
                                  )
        


    def parse_page(self, response):         
        #hxs = Selector(response)
        print("yolo")
# 
#         rows = hxs.xpath('//a[contains(@href,"CV")]')
#         print(len(rows))
#         for row in rows:
#             item = ApecItem()
#             url = row.extract()
#             item['urlCV'] = url
#             print(url) 
#             print(url)
#             yield item

class ClickSpider(BaseSpider):
            name = "click"
            allowed_domains = ["recruteurs.apec.fr"]
            start_urls = ['http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp']
            
            def parse(self,response):
                print("ClickSpider")
                print("ClickSpider")
                yield FormRequest(url = "http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp?PEGA_HRSM_704371172_0_0_doGoConsulterCV=doGoConsulterCV",
                                  method="POST"
                                  ,callback=CritereSpider.parse)
        
            def parse_page(self,response):
                print("boss")
                
                
                
class CritereSpider(BaseSpider):
    name = "criteres"
    allowed_domains = ["recruteurs.apec.fr"]
    start_urls = ['http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp?PEGA_HRSM_704371172_0_0_doGoConsulterCV=doGoConsulterCV']
            
    def parse(self,response):
       
        print("CritereSpider")
        print("CritereSpider") 
        yield FormRequest(url = "http://recruteurs.apec.fr/CV/Candidapec/ApecCreateRequete.jsp?PEGA_HRSM_1739906055_0_0_doSearchByCriteres=doSearchByCriteres"
                          ,method="POST"
                          ,callback=self.parse_page) #rajouter les criteres (voir formdata de LogSpider)
        
    def parse_page(self,response):
        hxs = Selector(response)
        res = []
        
        rows = hxs.xpath('//td[@class="titreCV"]/dl/dt/a/text()')
        print(len(rows))
        print(len(rows))
        for row in rows:
            item = ApecItem()
            url = row.extract()
            item['urlCV'] = url
            print(url) 
            print(url)
            res = res.append(item)
            
        print(len(res))
        
        
# class DLSpider(BaseSpider):
#     name = "downloader"
#     allowed_domains = ["recruteurs.apec.fr"]
#     start_urls = ['http://recruteurs.apec.fr/CV/Candidapec/ApecCreateRequete.jsp?PEGA_HRSM_1739906055_0_0_doSearchByCriteres=doSearchByCriteres']
#     
#     def parse(self,response):
#         yield FormRequest(url)
    
    
    
    
    
    