from xml.dom.minidom import Element
from selenium.webdriver.common.by import By

class Login_Page:
    def __init__(self,driver) :
        self.driver=driver
        self.username=(By.NAME,"username")
        self.password=(By.NAME,"password")
        self.loginbutton=(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
        self.forget_Pass_link=(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p")
        
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
        
    def login(self,name,passw):
        self.enter_username(name)
        self.enter_password(passw)
        self.click_loginbutton()
        
    def forget_pass_click(self):    
        self.driver.find_element(*self.forget_Pass_link).click()
        