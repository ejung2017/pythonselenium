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

driver.get("https://orteil.dashnet.org/cookieclicker/")
# This is a game where you need to click enough of the big cookie to purchase the items
# aim is to automate the clicks until I buy all the items -- each item's price goes up as the demand goes up 

#before clicking the cookie, the main page has a pop-up to select the language
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)
language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

#using the Inspector Element function, I found the id of the cookie = "bigCookie"
cookie_id = "bigCookie"
cookies_banner_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"

# validate the cookie_id exists 
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

cookie = driver.find_element(By.ID, cookie_id)

while True: 
    cookie.click()
    cookies_count = driver.find_element(By.ID, cookies_banner_id).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))

    #there's 4 products in the right section
    for i in range(4): 
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

        if not product_price.isdigit():
            continue

        #some prices are written as "1,000" so I need to remove the comma to make it "1000"
        product_price = int(product_price)

        if cookies_count >= product_price: 
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break 

time.sleep(5)



