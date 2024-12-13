import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select #This module will help us interact with elements that creates a dropdown
from selenium.common.exceptions import NoSuchElementException #Will help us handle fallback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Webdriver helps you start a desired web browser
drive = webdriver.Chrome()

#Within the browser, we can have a way to maximize our view
drive.maximize_window()

#Have a function that handles issues while loading a page, e.g connectivity issue
def retries_get(url, retries=3, delay=5):
    #Let's have a loop that tries to get a page
    for attempt in range(retries):
        try:
            drive.get(url)
            return
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                print(f"retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print("All attempts failed")
                raise

#Now let's use our function
retries_get('https://account.google.com/')

try:
    #Once inside the first page, is a good practice to accept cookies, let's do that
    #"glue-cookie-notification-bar__accept"
    time.sleep(5)
    cookieButton = drive.find_element(By.XPATH, "//button[@class='glue-cookie-notification-bar__accept']")
    cookieButton.send_keys(Keys.RETURN)
    

    #aria-label "Go to your Google Account"
    #Let's try if we can access a google account
    googleAcc = drive.find_element(By.PARTIAL_LINK_TEXT, "Create an account") #Prefer using  PARTIAL_LINK_TEXT instead of LINK_TEXT because of white spaces
    googleAcc.click()

    #Now let's us find input and enter our name
    time.sleep(5)
    firstName = drive.find_element(By.XPATH, '//input[@name="firstName"]')
    firstName.send_keys("Catlin")

    #let's skip surname for now and just click the next button
    nxt = drive.find_element(By.XPATH, '//button[@type="button"]')
    nxt.click()

    time.sleep(10)
    #Birthday setup
    dropDown = drive.find_element(By.ID, "month")

    #We a now going to create a Select object
    select = Select(dropDown)

    #Select the option with value '3'/or your preference birthmonth
    select.select_by_value('3') #month

    day = drive.find_element(By.XPATH, '//input[@name="day"]')
    day.send_keys("23") #day

    year = drive.find_element(By.XPATH, '//input[@name="year"]')

    year.send_keys("2000") #year

    #now let use select gennder
    gender = drive.find_element(By.ID, "gender")

    #create a select object
    selectGender = Select(gender)

    #select gender by value
    selectGender.select_by_value('2') #female
    time.sleep(5)

    #new next button
    nxtbtton = drive.find_element(By.XPATH, '//button[@type="button"]')

    nxtbtton.click()
    time.sleep(20) #sleep for another 20sec as we wait
    #There are two options: choose any random email or inputting a username
    #Let's handle them both
    try:
        email = WebDriverWait(drive, 10).until(
            EC.element_to_be_clickable((By.ID), "selectionc1")
        )

        email.click()
        time.sleep(3) #sleep for another 20sec as we wait
    except NoSuchElementException:
        #Here is where we fallBack incase this error occur - means the first option failed

        try:
            #next option for searching by username
            username = drive.find_element(By.NAME, 'Username')
            username.send_keys("cabracakida4590")
        except NoSuchElementException:
            print("Both options not available")

    #new next button
    nxtbtton = drive.find_element(By.XPATH, '//button[@type="button"]')

    nxtbtton.click()


    #password setup
    passwd = drive.find_element(By.NAME, "Passwd")
    passwdAgain = drive.find_element(By.NAME, "PasswdAgain")

    myPass = "CatlinJones@2000"
    passwd.send_keys(myPass)
    passwdAgain.send_keys(myPass)
    time.sleep(5)
    #new next button
    nxtbtton = drive.find_element(By.XPATH, '//button[@type="button"]')

    nxtbtton.click()
    time.sleep(200)

except Exception as e:
    print(e)