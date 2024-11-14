from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#in order to automate a browser, we need to use a webdriver and this is 
service = Service(executable_path="/Users/eunahjung/Documents/pythonselenium/chromedriver")
driver = webdriver.Chrome(service=service)

# https://sites.google.com/chromium.org/driver/
# download the driver and put the path in the executable_path
# intel mac -> download mac-x64 

driver.get("https://www.google.com")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("NewJeans" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "NewJeans"))
)

links = driver.find_element(By.PARTIAL_LINK_TEXT, "NewJeans")
links.click()

time.sleep(10)

driver.quit()
