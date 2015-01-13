from selenium import webdriver
from scrapy.contrib.spiders.init import InitSpider


class apecSelenium(InitSpider):
    name = "product_spider"
    allowed_domains = ["recruteurs.apec.fr"]
    start_urls = ["http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp?PEGA_HREF_950420318_0_0_doLogin=doLogin"]
    baseurl = "http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp?PEGA_HREF_950420318_0_0_doLogin=doLogin"
    login = "47179308"
    password = "6KPA43V8"
    keyword = "catia"
    region = []
    mobilite = ""
    salaire = ""
    disponibilite = ""
    fraicheur = ""
    nombreCV = 50 
    
    
    def __init__(self,login,password,keyword,region,mobilite,salaire,disponibilite,fraicheur,nombreCV):
        """Initialisation du spider"""
        self.login = login
        self.password = password
        self.keyword = keyword
        self.region = region
        self.mobilite = mobilite
        self.salaire = salaire
        self.disponibilite = disponibilite
        self.fraicheur = fraicheur
        self.nombreCV = nombreCV
        self.driver = webdriver.Firefox()
    
    def parse(self, response):
        
        self.driver.get(self.baseurl)
        
        """Login"""
        self.driver.find_element_by_id('login').clear()
        self.driver.find_element_by_id('login').send_keys(self.login)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(self.password) 
        login = self.driver.find_element_by_css_selector('.boutonSmall.floatRight.marginRight.noMarginBottom>a')
        mouseLogin = webdriver.ActionChains(self.driver)
        mouseLogin.move_to_element(login).click().perform()
        
        """Acces a la page de recherche"""
        buttonCV = self.driver.find_elements_by_css_selector('.button1>a')
        mouseRecherche = webdriver.ActionChains(self.driver)
        mouseRecherche.move_to_element(buttonCV[2]).click().perform()
        
        """Remplissage du formulaire"""
        """Mot-clef"""
        self.driver.find_element_by_id('autocomplete').clear()
        self.driver.find_element_by_id('autocomplete').send_keys(self.keyword)
   
        """Region"""
        #TODO
        
        """Mobilite"""
        #TODO
        
        """Salaire"""
        #TODO
        
        """Disponibilite"""
        #TODO
        
        """Fraicheur"""
        #TODO
        
        """nombreCV"""
        #TODO
        
        """Acces a la page des CVs"""
        bouttonRechercher = self.driver.find_element_by_css_selector('.button-search>a')
        mouseAccesCVS = webdriver.ActionChains(self.driver)
        mouseAccesCVS.move_to_element(bouttonRechercher).click().perform()