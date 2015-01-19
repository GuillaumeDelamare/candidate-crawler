# -*- coding: utf-8 -*-

from selenium import webdriver
from scrapy.contrib.spiders.init import InitSpider
from selenium.webdriver.common.keys import Keys
import time
import os


class apecSelenium(InitSpider):
    """congig du spider"""
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
#
        driver = webdriver.Firefox()        
      #  profile = webdriver.FirefoxProfile()
       # driver.profile.set_preference("driver.download.folderList", 2)
        driver.profile.set_preference("driver.download.manager.showWhenStarting", False)
       # driver.profile.set_preference("driver.download.dir", 'C:/Utilisateur/Jonathan/Téléchargement')
        driver.profile.set_preference("driver.helperApps.neverAsk.saveToDisk", 'application/pdf')

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
        
        
        """Enregistrer les liens des pages des CVs a telecharger"""
        compteur = 0
        boutonCVs = driver.find_elements_by_css_selector('.titreCV>dl>dt>a')
        clicOnglets = []
      
        webdriver.ActionChains(driver).click(boutonCVs[compteur]).perform()
        b=driver.find_element_by_css_selector(".cvDownload>a")
        webdriver.ActionChains(driver).click(b).perform()
#         while compteur < len(boutonCVs):
#             main_window = driver.current_window_handle
#             clicOnglets.append(webdriver.ActionChains(driver))
#             clicOnglets[compteur].key_down(Keys.LEFT_CONTROL+ Keys.SHIFT)
#             clicOnglets[compteur].click(boutonCVs[compteur])
#             clicOnglets[compteur].key_up(Keys.LEFT_CONTROL+ Keys.SHIFT)
#             clicOnglets[compteur].perform()
#             driver.switch_to_window(driver.current_window_handle)
#             #TODO
#             time.sleep(3)
#             driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
#             driver.switch_to_window(main_window)
#             compteur = compteur + 1
            
#         print(self.nombreCV)
#         while compteur in xrange(0,int(self.nombreCV)-1) and compteur < len(boutonCVs):
#             self.listePageCV.append(boutonCVs[compteur].get_attribute("href"))
#             compteur = compteur + 1
#             
#         """Parcoure les pages de telechargement desCVs"""
#         compteur2 = 0
#         while compteur2 < len(self.listePageCV):
#             driver.get(self.listePageCV[compteur2])
#             compteur2 = compteur2 + 1
#         """Fin du crawling"""
#         driver.close()