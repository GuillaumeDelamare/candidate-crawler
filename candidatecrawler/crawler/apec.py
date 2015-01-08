'''
Created on 8 janv. 2015

@author: Pierre
'''

from scrapy.http import FormRequest
from scrapy.item import Item, Field
from scrapy.selector import Selector

from scrapy.spider import BaseSpider
from twisted.python.util import println


class ApecItem(Item):
    urlCV = Field()
    println("bouh")


class CVSpider(BaseSpider):
    name = "CVFinder"
    allowed_domains = ["recruteurs.apec.fr"]
    start_urls = ['http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp?PEGA_HREF_950420318_0_0_doLogin=doLogin']


    def parse(self, response):
        
        formdata = {'PEGA_IMBT_12928340_0_0_doLogin':'47179308','PEGA_IMBT_24835201_0_0_doLogin':'6KPA43V8'}
        print("tata")
        yield FormRequest(url="http://recruteurs.apec.fr/CV/Candidapec/ApecCreateRequete.jsp?PEGA_HRSM_1851182314_0_0_doSearchByCriteres=doSearchByCriteres",
                                  method="POST",
                                  formdata=formdata,
                                  callback=self.parse_page,
                                  )
                #spider


    def parse_page(self, response):
        hxs = Selector(response)

        rows = hxs.xpath('//a')
        println(rows.__sizeof__())
        for row in rows:
            println("juste apres")
            item = ApecItem()
            url = row.extract()[0]
            item['urlCV'] = url
            println("toto")
            yield item