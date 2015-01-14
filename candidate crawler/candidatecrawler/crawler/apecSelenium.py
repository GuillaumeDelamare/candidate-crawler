# -*- coding: utf-8 -*-
from selenium import webdriver
from scrapy.contrib.spiders.init import InitSpider


class apecSelenium(InitSpider):
    name = "product_spider"
    allowed_domains = ["recruteurs.apec.fr"]
    start_urls = ["http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp?PEGA_HREF_950420318_0_0_doLogin=doLogin"]
    baseurl = "http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp?PEGA_HREF_950420318_0_0_doLogin=doLogin"
    login = "47179308"
    password = "6KPA43V8"
    keyword = ""
    region = []
    regions=["Toute la France","Alsace","Aquitaine","Auvergne","Basse-Normandie","Bourgogne","Bretagne","Centre","Champagne","Corse",
             "France Outre-Mer","Franche-Comté","Haute-Normandie","Ile-de-France","Languedoc-Roussillon",
             "Limousin","Lorraine","Midi-Pyrénées","Nord-Pas-de-Calais",
             "PACA","Pays de La Loire","Picardie","Poitou-Charentes","Rhône-Alpes"]
    
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
        
        
    
    def parse(self, response):
        """"Lancement du driver"""
        driver = webdriver.Firefox()
        #driver.set_window_position(-2000, -3000)
        driver.get(self.baseurl)
        
        """Login"""
        driver.find_element_by_id('login').clear()
        driver.find_element_by_id('login').send_keys(self.login)
        driver.find_element_by_id('password').clear()
        driver.find_element_by_id('password').send_keys(self.password) 
        login = driver.find_element_by_css_selector('.boutonSmall.floatRight.marginRight.noMarginBottom>a')
        mouseLogin = webdriver.ActionChains(driver)
        mouseLogin.move_to_element(login).click().perform()
        
        """Acces a la page de recherche"""
        buttonCV = driver.find_elements_by_css_selector('.button1>a')
        mouseRecherche = webdriver.ActionChains(driver)
        mouseRecherche.move_to_element(buttonCV[2]).click().perform()
        
        """Remplissage du formulaire"""
        """Mot-clef"""
        driver.find_element_by_id('autocomplete').clear()
        driver.find_element_by_id('autocomplete').send_keys(self.keyword)
   
        """Region"""
        if self.region.__contains__("Toute la France"):
            webdriver.ActionChains(driver).move_to_element(driver.find_element_by_id("franceEntiere")).click().perform()
    
        else:
            regionssite=driver.find_elements_by_css_selector('.normal>input')
        
            for k in range(0,len(self.regions)):
                if self.region.__contains__(self.regions[k]) :
                    webdriver.ActionChains(driver).move_to_element(regionssite[k-1]).click().perform()
                k=k+1
            
        """Mobilite"""
        #TODO:
        
        """Salaire"""
        #TODO:
        
        """Disponibilite"""
        #TODO:
        
        """Fraicheur"""
        #TODO:
        
        """Acces a la page des CVs"""
        bouttonRechercher = driver.find_element_by_css_selector('.button-search>a')
        mouseAccesCVS = webdriver.ActionChains(driver)
        mouseAccesCVS.move_to_element(bouttonRechercher).click().perform()
        
        """Enregistrer les liens des CVs a telecharger"""
        #Todo:
        
        """Telecharger les Cvs"""
        #TODO:
        
        """Fermeture de la fenetre"""
        driver.close()
        return "toto"
        