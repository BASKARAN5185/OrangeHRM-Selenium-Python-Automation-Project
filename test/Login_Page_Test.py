import os
import sys
from time import sleep, time

# ✅ Add the root directory of the project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.Login_Page import Login_Page
from selenium import webdriver


def login_with_credential():
    # ✅ Launch Chrome browser
    driver = webdriver.Chrome()
    
    # ✅ Navigate to the login page
    driver.get("https://stg.rms.mo.vc/web/login")
    
    # ✅ Create Login_Page object and perform login
    lg = Login_Page(driver)
    lg.enter_username("testingteam@gmail.com")
    lg.enter_password("Solution@456")
    lg.click_loginbutton()
    
    # ✅ Print the page title after login
    print(driver.title)
    
    # Optional: Close the browser after a few seconds
    driver.quit()

# ✅ Run the function when the script is executed
if __name__ == "__main__":
    login_with_credential()
