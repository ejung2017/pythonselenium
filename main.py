from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
import time

#in order to automate a browser, we need to use a webdriver and this is 
service = Service(executable_path="/Users/eunahjung/Documents/pythonselenium/chromedriver")
driver = webdriver.Chrome(service=service)

# https://sites.google.com/chromium.org/driver/
# download the driver and put the path in the executable_path
# intel mac -> download mac-x64 

driver.get("https://www.google.com")

time.sleep(10)

driver.quit()
