from xml.dom.minidom import Element
from selenium.webdriver.common.by import By

class Login_Page:
    def __init__(self,driver) :
        self.driver=driver
        self.username=(By.NAME,"username")
        self.password=(By.NAME,"password")
        self.loginbutton=(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
        
    def enter_username(self,username):
        user1=self.driver.find_element(*self.username)
        user1.clear()
        user1.send_keys(username)
        
    def enter_password(self,password):
        password1=self.driver.find_element(*self.password)
        password1.clear()
        password1.send_keys(password)   
    
    def click_loginbutton(self):
        self.driver.find_element(*self.loginbutton).click()
        
        
        
               