
from selenium import webdriver


baseurl = 'http://recruteurs.apec.fr/Accueil/ApecIndexAccueil.jsp?PEGA_HREF_950420318_0_0_doLogin=doLogin'
username = "47179308"
password = "6KPA43V8"

xpaths = { 'usernameTxtBox' : "//div[@id='login']",
           'passwordTxtBox' : "//div[@id='password']",
           'submitButton' :   "//input[@name='signeOn']"
         }

mydriver = webdriver.Firefox()
mydriver.get(baseurl)
mydriver.maximize_window()

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

