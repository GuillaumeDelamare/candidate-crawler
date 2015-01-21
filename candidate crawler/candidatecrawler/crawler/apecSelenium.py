# -*- coding: utf-8 -*-

from candidatecrawler.core import toolbox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import os
import csv
from email import email



class apecSelenium:
    """config du spider"""
    
    
    
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
        self.disponibiliteStr=disponibilite
        
        if disponibilite.__contains__("Immediate"):
            self.disponibilite.append(0)
            
        if disponibilite.__contains__( "Moins de 3 mois"):
            self.disponibilite.append(1)
            
        if disponibilite.__contains__( "Entre 3 et 6 mois"):
            self.disponibilite.append(2)
            
        if disponibilite.__contains__( "Plus de 6 mois"):
            self.disponibilite.append(3) 
        
        self.name = "product_spider"
        self.allowed_domains = ["recruteurs.apec.fr"]
        self.start_urls = ["http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp?PEGA_HREF_950420318_0_0_doLogin=doLogin"]
        self.baseurl = "http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp?PEGA_HREF_950420318_0_0_doLogin=doLogin"
   
        """Instance propre au site de l'APEC"""
        self.regions=["Toute la France","Alsace","Aquitaine","Auvergne","Basse-Normandie","Bourgogne","Bretagne","Centre","Champagne","Corse",
                 "France Outre-Mer", "Franche-Comté","Haute-Normandie","Ile-de-France","Languedoc-Roussillon",
                 "Limousin","Lorraine","Midi-Pyrénées","Nord-Pas-de-Calais",
                 "PACA","Pays de La Loire","Picardie","Poitou-Charentes","Rhône-Alpes"]
        self.disponibilites = ['0','1','2','3']
        
        """Aretourner"""
        self.listePageCV = []
        self.listeLienCV = []
        self.ligneCSV = [["nom du fichier","reference","nom du candidat","email","salaire","mobilite","disponibilite","mise a jour"]]
            
    
    def parse(self):
        """"Lancement du driver"""
        path = toolbox.getconfigvalue("GENERALPARAMETERS", "dbfile")+os.sep+self.datetime.strftime("%Y-%m-%d-%H-%M-%S")
        os.mkdir(path)
        
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList",2)
        profile.set_preference("browser.download.manager.showWhenStarting",False)
        profile.set_preference("browser.download.dir", path+os.sep+"CV")
        profile.set_preference("pdfjs.disabled",True)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf, application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document, application/rtf")
        driver = webdriver.Firefox(firefox_profile=profile)
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
        
        for k in range(24,24+len(self.disponibilites)):
                if self.disponibilite.__contains__(self.disponibilites[k-24]) :
                    webdriver.ActionChains(driver).move_to_element(disponibilitesite[k-1]).click().perform()
                k=k+1
            
        
        
        """Fraicheur"""
        fraicheursite=driver.find_elements_by_css_selector('.contentInside>select>option')
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
            try:
                    
                #permet d'ouvrir les onglets et d'aller sur les pages des CVs
                main_window = driver.current_window_handle
                clicOnglets.append(webdriver.ActionChains(driver))
                clicOnglets[compteur].key_down(Keys.LEFT_CONTROL+ Keys.SHIFT)
                clicOnglets[compteur].click(boutonCVs[compteur])
                clicOnglets[compteur].key_up(Keys.LEFT_CONTROL+ Keys.SHIFT)
                clicOnglets[compteur].perform()
                driver.switch_to_window(driver.current_window_handle)
                    
                #fait un tableau avec les données         
                rightBox=driver.find_elements_by_css_selector('.cvDetails>p') #boite de droite sur le site de l'APEC
                leftBox=driver.find_elements_by_css_selector('.cvEtatCivil>p') #boite de gauche
                
                "nom du fichier","reference","nom du candidat","telephone","email","salaire","mobilite","disponibilite","mise a jour"
                
                ref=(rightBox[0].text[18:]+" ").encode('utf-8')
                try:
                    candidateName=driver.find_element_by_css_selector('.cvEtatCivil>p>strong').text.encode('utf-8')
                except IndexError:
                    candidateName="Anonyme"
                try:
                    fileName=rightBox[2].text[11:].encode('utf-8')
                except IndexError:
                    fileName="error"
                try:
                    email=leftBox[len(leftBox)-1].text[9:].encode('utf-8')
                except IndexError:
                    email="Anonyme"
                salaire=self.salaire
                mobi=self.mobilite
                dispo=self.disponibiliteStr
                try:
                    update=rightBox[1].text[31:].encode('utf-8')
                except IndexError:
                    update="Date inconnue"
                #Remplissage csv
                self.ligneCSV.append([fileName,ref,candidateName,email,salaire,mobi,dispo,update])  
                
                    
                #action qui se déroule sur la page du CV (excel, telechargement)
                #telechargement du CV
                telechargeCV = driver.find_element_by_css_selector(".cvDownload>a")
                webdriver.ActionChains(driver).click(telechargeCV).perform()
                time.sleep(2)
                   
                #referme l'ongler dans lequel on a travaillé et incrémente
                driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
                driver.switch_to_window(main_window)
                compteur = compteur + 1
            except _:
                print("erreur serveur(probablement interne), relancez la recherche")
            
            
            
        """Fin du crawling"""
        driver.close()
        
        #créer et remplir le csv avec le tableau de données
        with open(path+os.sep+"rapport.csv","w") as database: #crée le fichier csv et l'ouvre
       
            writer=csv.writer(database)
            writer.writerows(self.ligneCSV)

        
        
