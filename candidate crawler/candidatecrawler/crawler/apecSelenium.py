# -*- coding: utf-8 -*-

from candidatecrawler.core import toolbox
from selenium import webdriver
from scrapy.contrib.spiders.init import InitSpider
from selenium.webdriver.common.keys import Keys
import time
import datetime
import os


class apecSelenium(InitSpider):
    """config du spider"""
    name = "product_spider"
    allowed_domains = ["recruteurs.apec.fr"]
    start_urls = ["http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp?PEGA_HREF_950420318_0_0_doLogin=doLogin"]
    baseurl = "http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp?PEGA_HREF_950420318_0_0_doLogin=doLogin"
   
    """Instance propre au site de l'APEC"""
    regions=["Toute la France","Alsace","Aquitaine","Auvergne","Basse-Normandie","Bourgogne","Bretagne","Centre","Champagne","Corse",
             "France Outre-Mer", "Franche-Comté","Haute-Normandie","Ile-de-France","Languedoc-Roussillon",
             "Limousin","Lorraine","Midi-Pyrénées","Nord-Pas-de-Calais",
             "PACA","Pays de La Loire","Picardie","Poitou-Charentes","Rhône-Alpes"]
    disponibilites = ['0','1','2','3']
    
    """Aretourner"""
    listePageCV = []
    listeLienCV = []
    ligneCSV = []
    
    
    def __init__(self,login,password,keyword,region,mobilite,salaire,disponibilite,fraicheur,nombreCV):
        """Initialisation du spider"""
        self.login = login
        self.password = password
        self.keyword = str(keyword)
        self.region = []
        for i in region:
            self.region.append(str(i))
        self.mobilite = str(mobilite)
        self.salaire = str(salaire)
        self.fraicheur = str(fraicheur)
        self.nombreCV = nombreCV
        self.disponibilite = []
        self.datetime = datetime.datetime.now()
        
        
        if disponibilite.__contains__("Immediate"):
            self.disponibilite.append(0)
            
        if disponibilite.__contains__( "Moins de 3 mois"):
            self.disponibilite.append(1)
            
        if disponibilite.__contains__( "Entre 3 et 6 mois"):
            self.disponibilite.append(2)
            
        if disponibilite.__contains__( "Plus de 6 mois"):
            self.disponibilite.append(3) 
        
        
    
    def parse(self, response):
        """"Lancement du driver"""
        path = toolbox.getconfigvalue("GENERALPARAMETERS", "dbfile")+os.sep+self.datetime.strftime("%Y-%m-%d-%H-%M-%S")
        os.mkdir(path)
        
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList",2)
        profile.set_preference("browser.download.manager.showWhenStarting",False)
        profile.set_preference("browser.download.dir", path+os.sep+"CV")
        profile.set_preference("pdfjs.disabled",True)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf, application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        driver = webdriver.Firefox(firefox_profile=profile)
        driver.set_window_position(-2000, -3000)
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
        mobilitesite=driver.find_elements_by_css_selector('.selectSize1>option')
        if self.mobilite == 0:
            webdriver.ActionChains(driver).move_to_element(mobilitesite[6]).click().perform()
        if self.mobilite == 1:
            webdriver.ActionChains(driver).move_to_element(mobilitesite[7]).click().perform()
        if self.mobilite == 2:
            webdriver.ActionChains(driver).move_to_element(mobilitesite[8]).click().perform()
        if self.mobilite == 3:
            webdriver.ActionChains(driver).move_to_element(mobilitesite[9]).click().perform()
        if self.mobilite == 4:
            webdriver.ActionChains(driver).move_to_element(mobilitesite[10]).click().perform()
        if self.mobilite == 5:
            webdriver.ActionChains(driver).move_to_element(mobilitesite[11]).click().perform()    
        
        """Salaire"""
        salairesite=driver.find_elements_by_css_selector('.selectSize1>option')
        if self.salaire == 0:
            webdriver.ActionChains(driver).move_to_element(salairesite[12]).click().perform()
        if self.salaire == 1:
            webdriver.ActionChains(driver).move_to_element(salairesite[13]).click().perform()
        if self.salaire == 2:
            webdriver.ActionChains(driver).move_to_element(salairesite[14]).click().perform()
        if self.salaire == 3:
            webdriver.ActionChains(driver).move_to_element(salairesite[15]).click().perform()
        if self.salaire == 4:
            webdriver.ActionChains(driver).move_to_element(salairesite[16]).click().perform()
        if self.salaire == 5:
            webdriver.ActionChains(driver).move_to_element(salairesite[17]).click().perform()   

            
        """Disponibilite"""
        disponibilitesite=driver.find_elements_by_css_selector('.normal>input')
        print('bouboubbb')
        print(disponibilitesite)
        for k in range(24,24+len(self.disponibilites)):
                if self.disponibilite.__contains__(self.disponibilites[k-24]) :
                    webdriver.ActionChains(driver).move_to_element(disponibilitesite[k-1]).click().perform()
                k=k+1
            
        
        
        """Fraicheur"""
        fraicheursite=driver.find_elements_by_css_selector('.contentInside>select>option')
        self.log("dlqghljghljsw")
        self.log(fraicheursite)
        if self.fraicheur == 0:
            webdriver.ActionChains(driver).move_to_element(fraicheursite[0]).click().perform()
        if self.fraicheur == 1:
            webdriver.ActionChains(driver).move_to_element(fraicheursite[1]).click().perform()
        if self.fraicheur == 2:
            webdriver.ActionChains(driver).move_to_element(fraicheursite[2]).click().perform()
        if self.fraicheur == 3:
            webdriver.ActionChains(driver).move_to_element(fraicheursite[3]).click().perform()
        
        
        """Acces a la page des CVs"""
        bouttonRechercher = driver.find_element_by_css_selector('.button-search>a')
        mouseAccesCVS = webdriver.ActionChains(driver)
        mouseAccesCVS.move_to_element(bouttonRechercher).click().perform()
        boutton100CVs = driver.find_elements_by_css_selector('.noPadding.boxContent>ul>li>select>option')
        mouse100CVs = webdriver.ActionChains(driver)
        mouse100CVs.move_to_element(boutton100CVs[3]).click().perform()
        
        
        """Sauvergarde les CVs et crée le Excel"""
        boutonCVs = driver.find_elements_by_css_selector('.titreCV>dl>dt>a')
        
        clicOnglets = []
        compteur = 0
        
        
        while compteur in xrange(0,int(self.nombreCV)) and compteur < len(boutonCVs): #va
            #permet d'ouvrir les onglets et d'aller sur les pages des CVs
            main_window = driver.current_window_handle
            clicOnglets.append(webdriver.ActionChains(driver))
            clicOnglets[compteur].key_down(Keys.LEFT_CONTROL+ Keys.SHIFT)
            clicOnglets[compteur].click(boutonCVs[compteur])
            clicOnglets[compteur].key_up(Keys.LEFT_CONTROL+ Keys.SHIFT)
            clicOnglets[compteur].perform()
            driver.switch_to_window(driver.current_window_handle)
            
            #faire un tableau avec les données
            #TODO a toi de jouer recupere les donnes sur la page, vois dans le raport final pour l'ordre des champs du csv

            
            #action qui se déroule sur la page du CV (excel, telechargement)
            #telechargement du CV
            telechargeCV = driver.find_element_by_css_selector(".cvDownload>a")
            webdriver.ActionChains(driver).click(telechargeCV).perform()
            time.sleep(2)
            
            #referme l'ongler dans lequel on a travaillé et incrémente
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
            driver.switch_to_window(main_window)
            compteur = compteur + 1
            
        
            
        """Fin du crawling"""
        driver.close()
        
        #créer et remplir le csv avec le tableau de données
        database = open(path+os.sep+"rapport.csv","w") #crée le fichier csv et l'ouvre
        #TODO a toi de jouer il faut remplir le csv
        database.close()
        
