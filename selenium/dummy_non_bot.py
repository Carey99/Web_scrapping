import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Random delay function
def random_delay():
    time.sleep(random.uniform(1, 3))

# Configure WebDriver
chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

drive = webdriver.Chrome(options=chrome_options)

# Bypass Selenium detection
drive.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
    """
})

# Start the script
drive.maximize_window()

# Retry loading the page
def retries_get(url, retries=3, delay=5):
    for attempt in range(retries):
        try:
            drive.get(url)
            return
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print("All attempts failed")
                raise

retries_get('https://account.google.com/')

try:
    random_delay()

    # Accept cookies
    cookieButton = WebDriverWait(drive, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='glue-cookie-notification-bar__accept']"))
    )
    actions = ActionChains(drive)
    actions.move_to_element(cookieButton).perform()  # Simulate mouse movement
    random_delay()
    cookieButton.click()

    # Click on "Create an account"
    googleAcc = drive.find_element(By.PARTIAL_LINK_TEXT, "Create an account")
    random_delay()
    googleAcc.click()

    # Input first name
    firstName = WebDriverWait(drive, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@name="firstName"]'))
    )
    firstName.send_keys("Catlin")
    random_delay()

    # Click the next button
    nxt = drive.find_element(By.XPATH, '//button[@type="button"]')
    random_delay()
    nxt.click()

    # Additional steps (e.g., birthday, username, etc.)...
    # Ensure each interaction has random delays and scroll-to-view where necessary

except TimeoutException as te:
    print("Timeout occurred:", te)
except Exception as e:
    print("An error occurred:", e)
finally:
    drive.quit()
