from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Create a Service object using the ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Go to Google
driver.get("https://stg.rms.mo.vc/")
driver.maximize_window()
driver.implicitly_wait(30)

# Login Future Test
print("Page title:", driver.title)
username=driver.find_element(By.NAME,"login")
username.send_keys("testingteam@gmail.com")
password=driver.find_element(By.NAME,"password")
password.send_keys("Solution@456")
Login=driver.find_element(By.XPATH,"//*[@id='wrapwrap']/main/div/div/div/div/div/form/div[3]/button")
print(Login.text)
Login.click()

home_page_logo=driver.find_element(By.XPATH, "//*[@id='menu-dropdown']/li[1]/a/span[2]")
print(home_page_logo.text)
assert home_page_logo is not None

# If you know something about the button's class, text, or id:
Jd_create_button = driver.find_element(By.XPATH, "//button[contains(text(), 'New')]")

Jd_create_button.click()

time.sleep(5)

# driver.quit()



