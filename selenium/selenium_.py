#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify the path to the ChromeDriver executable
chrome_driver_path = './chromedriver.exe'
service = Service(chrome_driver_path)

# Specify Chrome options
options = webdriver.ChromeOptions()
options.binary_location = './chrome.exe'
options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Redirect Selenium to Google and perform a search query
try:
    driver.get('https://google.com')
    print('...navigating')
except Exception as e:
    print(e)
finally:
    # Close the browser
    driver.quit()
