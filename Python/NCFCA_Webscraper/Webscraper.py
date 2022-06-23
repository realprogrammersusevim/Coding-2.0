# TODO: Good and bad news. If a website, like ncfca.org uses Javascript to
# locally load dynamic content then mechanical soup can't deal with that. It
# will only use the static webpage that was first loaded. The solution however
# is to use a hybrid method to load the page with Selenium and then use
# Beautiful Soup and Mechanical Soup for the HTML parsing and interaction.
import os
import pickle
from time import sleep

import applescript
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml

print('How many minutes would you like the script to run for?')
minutes = input()

try:
    minutes = int(minutes)
except:
    print('Please put in the number of minutes you would like this to run for')
    minutes = int(input())

repititions = minutes / 2
repititions = round(repititions)

# Starts a browser session I need to clean all of this code up.
options = webdriver.ChromeOptions()
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
DRIVER_PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

# Pulls up the ncfca.org login window
driver.get("https://portal.ncfca.org")
driver.implicitly_wait(30)

try:
    with open('my_secret_creds.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
except:
    with open('credentials.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

# Finds the text box where you enter your email by the html name, clicks it,
# and then fills it out with my email.
email_login = driver.find_element(By.ID, 'mat-input-9')
email_login.click()
email_login.send_keys(data.get('username'))

# Finds the text box where you enter your password by the html name, clicks it,
# and then fills it out with my email.
password_login = driver.find_element(By.ID, "mat-input-10")
password_login.click()
password_login.send_keys(data.get('password'))
sleep(2)

# Find the Log In button by its Xpath and then click it.
login_button = driver.find_element(
    By.XPATH, '''/html/body/app-root/mat-sidenav-container/mat-sidenav-content/div/app-sign-in/div/div/div[1]/button[1]''')
login_button.click()
driver.implicitly_wait(30)

# Finds the Enter Tournament button by its Xpath and then clicks on it.
def click_tournament_enter():
    enter_tournament = driver.find_element(
        By.XPATH, data.get('enter_tournament_button_xpath'))
    enter_tournament.click()


try:
    click_tournament_enter()
except:
    sleep(10)
    click_tournament_enter()

with open('var_storage.p', 'xw') as f:
    f.pickle('0')

for i in range(repititions):
    html = driver.page_source   # Renders the JS and stores it as static HTML
    # Sets the rendered JS to a Beautiful Soup object
    soup = BeautifulSoup(html, "html.parser")

    # No more website interaction is needed, so we can safely quit the driver
    driver.quit()

    # Finds every piece of content that has the class name of a posted listing
    activated_postings = soup.find_all(
        class_='schedule-list-item active ng-star-inserted')

    # Checks if there are any more listings have been posted
    count = 0
    for posting in activated_postings:
        count += 1

    # Currently it's just using a text file to store how many listings were
    # posted last time. I may need a better solution like pickle.
    with open('var_storage.p', 'r') as f:
        stored_number = f.unpickle()

    # If there are more listings posted now then there were before than it
    # executes an AppleScript which sends a notification and then updates the
    # number.
    if stored_number < count:
        send_notification = applescript.run('''display notification "New listings have been
        posted." with title "New Listings"''')
        with open('var_storage.p', 'w') as f:
            f.pickle(count)

    sleep(120)
    driver.refresh()

os.remove('var_storage.txt')
