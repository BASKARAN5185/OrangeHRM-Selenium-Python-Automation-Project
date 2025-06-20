import os
import sys
from typing import Self
import unittest
from selenium import webdriver

# Add the root directory of the project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.Login_Page import Login_Page
class Login_Page_Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(15)
        cls.driver.minimize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.login_page = Login_Page(self.driver)

    def test_Invalid_login(self):
        self.login_page.enter_username("testiteam@gmail.com")
        self.login_page.enter_password("Solon@456")
        self.login_page.click_loginbutton()
       # self.assertIn("Dashboard", self.driver.title)
    
    def test_Invalid_username(self):
        self.login_page.enter_password("Admi_n")
        self.login_page.enter_password("admin123")   
        self.login_page.click_loginbutton()
        print(self.driver.title)
        
    def test_Invalid_Password(self):
        self.login_page.enter_username("Admin")
        self.login_page.enter_password("jhjhgj")
        self.login_page.click_loginbutton()
        
    def test_empty_username(self):
        self.login_page.enter_username("")
        self.login_page.enter_password("admin123")  
        self.login_page.click_loginbutton() 
        
    def test_empty_Password(self):
        self.login_page.enter_username("Admin")
        self.login_page.enter_password("")  
        self.login_page.click_loginbutton()
     
    def test_empty_usernameandpassword(self):
        self.login_page.enter_username("")
        self.login_page.enter_password("")  
        self.login_page.click_loginbutton()   
        
    def test_forgetpassworkclick(self):
        self.login_page.forget_pass_click()
                     
        
if __name__ == "__main__":
    unittest.main()
    