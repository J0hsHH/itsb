from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
class itsb:

    def __init__(self):
     self.driver = webdriver.Chrome()
    def login_it(self):				 	       		#login in with itslearning
     self.driver.get('https://www.itslearning.com/welcome.aspx')
     #sleep(1)
     lb = self.driver.find_element_by_xpath('/html/body/main/form/section[1]/div[1]/section/span/input[1]')
     lb.send_keys('Danielsen Skoler') # edit the school 
     #lb.send_keys(Keys.ENTER)
     sleep(1.3)
     llb = self.driver.find_element_by_xpath('/html/body/main/form/section[1]/input') #prints the login button (lbb stands for login button )
     sleep(0.5)
     llb.click() 
     Logg_på_med_Feide = self.driver.find_element_by_xpath('/html/body/main/form/section/section[2]/ul/li[3]/div/a')
     Logg_på_med_Feide.click() 
     
     #feide_login
     
     feide_username = self.driver.find_element_by_xpath('/html/body/div/article/section[2]/div[1]/form/div[1]/input')
     feide_password = self.driver.find_element_by_xpath('/html/body/div/article/section[2]/div[1]/form/div[2]/input')
     feide_username.send_keys('YOUR USERNAME') # THIS IS YOUR USERNAME
     feide_password.send_keys('YOUR PASSWORD') # THIS IS YOUR PASSWORD
     
     feide_login = self.driver.find_element_by_xpath('/html/body/div/article/section[2]/div[1]/form/button')
     feide_login.click()

     # you have logde in to it's learning (let's spam)
     
     sleep(2)
     chat_synbol = self.driver.find_element_by_xpath('/html/body/form/header/div[1]/nav[3]/ul/li[3]')
     chat_synbol.click()
     
     
     
     en = self.driver.find_element_by_xpath('//*[@id="personal-menu__instant-message"]/div[2]/div[1]/div[4]/ul/li[1]/button')
     to = self.driver.find_element_by_xpath('//*[@id="personal-menu__instant-message"]/div[2]/div[1]/div[4]/ul/li[2]/button')
     tre = self.driver.find_element_by_xpath(' //*[@id="personal-menu__instant-message"]/div[2]/div[1]/div[4]/ul/li[3]/button')
     fire = self.driver.find_element_by_xpath('//*[@id="personal-menu__instant-message"]/div[2]/div[1]/div[4]/ul/li[4]/button')
     fem = self.driver.find_element_by_xpath(' //*[@id="personal-menu__instant-message"]/div[2]/div[1]/div[4]/ul/li[5]/button')
     
     
     
     
     
     
bot = itsb()
bot.login_it()

