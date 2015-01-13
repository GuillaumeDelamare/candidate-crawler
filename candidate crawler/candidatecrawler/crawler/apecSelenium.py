
from selenium import webdriver
from cssselect.parser import Selector

class apecSelenium:
    
    baseurl = 'http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp?PEGA_HREF_950420318_0_0_doLogin=doLogin'
    username = ""
    password = ""
    criteres = []
    
    def __init__(self,login,passwd,criteres):
        self.username=login
        self.password=passwd
        self.criteres=criteres

    
    
    xpaths = { 'usernameTxtBox' : "//div[@id='login']",
               'passwordTxtBox' : "//div[@id='password']",
               'submitButton' :   "//input[@name='signeOn']"
             }
    
    mydriver = webdriver.Firefox()
    mydriver.get(baseurl)
    
    
    #Clear Username TextBox if already allowed "Remember Me" 
    mydriver.find_element_by_id('login').clear()
    
    #Write Username in Username TextBox
    mydriver.find_element_by_id('login').send_keys(username)
    
    #Clear Password TextBox if already allowed "Remember Me" 
    mydriver.find_element_by_id('password').clear()
    
    #Write Password in password TextBox
    mydriver.find_element_by_id('password').send_keys(password)
    
    #Click Login button
    
    # You need a mouse to hover the span elements here
    mouse = webdriver.ActionChains(mydriver)    
    
    
    
        
    
    button=mydriver.find_element_by_css_selector('.boutonSmall.floatRight.marginRight.noMarginBottom>a')
    print(button)
    
    # Then you hover on span element by mouse and click on it:
    mouse.move_to_element(button).click().perform()
    
    
    mouse2=webdriver.ActionChains(mydriver)
    # for window in mydriver.window_handles:
    #     mydriver.switch_to_window(window)
    
    
     
    buttonCV=mydriver.find_elements_by_css_selector('.button1>a')
    print(buttonCV)
    mouse2.move_to_element(buttonCV[2]).click().perform()
    
    
    
    mouse3=webdriver.ActionChains(mydriver)
    if not criteres[0]==list():
        mydriver.find_element_by_id('autocomplete').clear()
        mydriver.find_element_by_id('autocomplete').send_keys(criteres[0])
    
    region = criteres[1]
    
    for i in range(1,24):
        if not region[i]=="vide":
            mouse3.move_to_element(mydriver.find_element_by_id(region[i])).click().perform()
    
    
    if not criteres[2]==list():
        mydriver.find_element_by_id('autocomplete').clear()
        mydriver.find_element_by_id('autocomplete').send_keys(criteres[0])
    
    if not criteres[3]==list():
        mydriver.find_element_by_id('autocomplete').clear()
        mydriver.find_element_by_id('autocomplete').send_keys(criteres[0])
    
    if not criteres[4]==list():
        mydriver.find_element_by_id('autocomplete').clear()
        mydriver.find_element_by_id('autocomplete').send_keys(criteres[0])
    
    if not criteres[5]==list():
        mydriver.find_element_by_id('autocomplete').clear()
        mydriver.find_element_by_id('autocomplete').send_keys(criteres[0])
    
    if not criteres[6]==list():
        mydriver.find_element_by_id('autocomplete').clear()
        mydriver.find_element_by_id('autocomplete').send_keys(criteres[0])
    
        
    
    
    
    
    
    
    
    
    
    
