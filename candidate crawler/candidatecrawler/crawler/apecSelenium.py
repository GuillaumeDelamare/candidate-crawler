from selenium import webdriver
from scrapy.contrib.spiders.init import InitSpider
from scrapy.selector import Selector

class apecSelenium(InitSpider):
    """congig du spider"""
    name = "product_spider"
    allowed_domains = ["recruteurs.apec.fr"]
    start_urls = ["http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp?PEGA_HREF_950420318_0_0_doLogin=doLogin"]
    baseurl = "http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp?PEGA_HREF_950420318_0_0_doLogin=doLogin"
    """parametre du spider"""
    login = "47179308"
    password = "6KPA43V8"
    keyword = ""
    region = []
    mobilite = 0
    salaire = 0
    disponibilite = []
    fraicheur = 0
    nombreCV = 50 
    """Instance propre au site de l'APEC"""
    regions=["Toute la France","Alsace","Aquitaine","Auvergne","Basse-Normandie","Bourgogne","Bretagne","Centre","Champagne","Corse",
             "France Outre-Mer","Franche-Comté","Haute-Normandie","Ile-de-France","Languedoc-Roussillon",
             "Limousin","Lorraine","Midi-Pyrénées","Nord-Pas-de-Calais",
             "PACA","Pays de La Loire","Picardie","Poitou-Charentes","Rhône-Alpes"]
    disponibilites = ['0','1','2','3']
    
    
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
        
          
        """Enregistrer les liens des CVs a telecharger"""
        #TODO
#         hxs = Selector('driver.current_url()')
#         res = list()
#         rows = hxs.xpath("//div[@id='chenillard']")
#         print(rows[0])
#         print(len(rows))
#         for row in rows:
#             url = row.extract()
#             res = res.append(url)
#         print(res)    
#         return res
#           
#         """Fermeture de la fenetre"""
#         driver.close()