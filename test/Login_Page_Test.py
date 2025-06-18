import os
import sys
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

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("https://stg.rms.mo.vc/web/login")
        self.login_page = Login_Page(self.driver)

    def test_valid_login(self):
        self.login_page.enter_username("testingteam@gmail.com")
        self.login_page.enter_password("Solution@456")
        self.login_page.click_loginbutton()
        self.assertIn("Dashboard", self.driver.title)

if __name__ == "__main__":
    unittest.main()
