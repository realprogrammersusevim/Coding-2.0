from lib2to3.pgen2 import driver
from operator import contains
from re import T
from tokenize import Name
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.color import Color
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from time import sleep

# Starts a browser session
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))

# Pulls up the ncfca.org login window
driver.get("https://portal.ncfca.org")
driver.implicitly_wait(30)

# Finds the text box where you enter your email by the html name, clicks it, and then fills it out with my email.
email_login = driver.find_element(By.ID, "mat-input-9")
email_login.click()
email_login.send_keys("jonathanmilligan42@icloud.com")

# Finds the text box where you enter your password by the html name, clicks it, and then fills it out with my email.
password_login = driver.find_element(By.ID, "mat-input-10")
password_login.click()
password_login.send_keys("clVy>VA:65")
sleep(2)

# Find the Log In button by its Xpath and then click it.
login_button = driver.find_element(
    By.XPATH, '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/div/app-sign-in/div/div/div[1]/button[1]')
login_button.click()

# Finds the Enter Tournament button by its Xpath and then clicks on it.
enter_tournament = driver.find_element(
    By.XPATH, '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/app-dashboard-family/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[4]/div/button[2]')
enter_tournament.click()

# This whole section is supposed to iterate over each of the postings until it reaches the end.
xpath_number_of_current_posting = 1
color_of_current_posting_being_checked = "rgba(0, 0, 0, 0)"


current_posting_being_checked = driver.find_elements(
    By.CLASS_NAME, '"schedule-list-item active ng-star-inserted"')
print(current_posting_being_checked)


driver.quit()
