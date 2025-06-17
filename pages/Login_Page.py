from selenium.webdriver.common.by import By

class Login_Page:
    def __init__(self,driver) :
        self.driver=driver
        self.username=(By.ID,"login")
        self.password=(By.ID,"password")
        self.loginbutton=(By.XPATH,"//*[@id='wrapwrap']/main/div/div/div/div/div/form/div[3]/button")
        
    def enter_username(self,username):
        self.driver.find_element(*self.username).send_keys(username)
        
        
    def enter_password(self,password):
        self.driver.find_element(*self.password).send_keys(password) 
        
    def click_loginbutton(self):
        self.driver.find_element(*self.loginbutton).click()
        
        
        
               