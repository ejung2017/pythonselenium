# Cookie Clicker using python selenium

Create the virtual environment 
```
python3 -m venv .venv
```

Install Selenium 
```
python3 -m venv path/to/venv
source path/to/venv/bin/activate
python3 -m pip install selenium
```

# Aim
1. Cookie Clicker is an web app game where you click the big cookie to purchase products.
2. The prices of the product gradually increases once the demand goes up, so this will enable the products to interchange the order and let the automated script to click all the products at least once.
3. The program will end (break) once all 4 products have been purchased.

# Steps
1. Install Selenium package and other libraries needed.
2. Download the webdriver (Chromedriver)
3. Using 'Inspect' in Chrome, find all the necessary IDs or Class names when finding elements
4. Use a for loop to automatically click the big cookie and also click the products to purchase. 
