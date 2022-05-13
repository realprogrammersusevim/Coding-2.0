# TODO: Good and bad news. If a website, like ncfca.org uses Javascript to
# locally load dynamic content then mechanical soup can't deal with that. It
# will only use the static webpage that was first loaded. The solution however
# is to use a hybrid method to load the page with Selenium and then use
# Beautiful Soup and Mechanical Soup for the HTML parsing and interaction.
import os

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import applescript

print('How many minutes would you like the script to run for?')
minutes = input()
minutes = int(minutes)
repititions = minutes / 2
repititions = round(repititions)

# Starts a browser session I need to clean all of this code up. It's partly
# from Stack Overflow and then heavily edited by Jonathan. Some of it is now
# unnecessary. This is the problem with coding. It's awful code, but i t does
# work so I don't want to touch it.
options = webdriver.ChromeOptions()
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
DRIVER_PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

# Pulls up the ncfca.org login window
driver.get("https://portal.ncfca.org")
driver.implicitly_wait(30)

# Finds the text box where you enter your email by the html name, clicks it,
# and then fills it out with my email.
email_login = driver.find_element(By.ID, 'mat-input-9')
email_login.click()
email_login.send_keys("jonathanmilligan42@icloud.com")

# Finds the text box where you enter your password by the html name, clicks it,
# and then fills it out with my email.
password_login = driver.find_element(By.ID, "mat-input-10")
password_login.click()
password_login.send_keys("clVy>VA:65")
sleep(2)

# Find the Log In button by its Xpath and then click it.
login_button = driver.find_element(
    By.XPATH, '''/html/body/app-root/mat-sidenav-container/mat-sidenav-content/div/app-sign-in/div/div/div[1]/button[1]''')
login_button.click()
driver.implicitly_wait(30)

# Finds the Enter Tournament button by its Xpath and then clicks on it.
def click_tournament_enter():
    enter_tournament = driver.find_element(By.XPATH, '''/html/body/app-root/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/app-dashboard-family/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[5]/div/button[2]''')
    enter_tournament.click()


try:
    click_tournament_enter()
except:
    sleep(10)
    click_tournament_enter()

f = open('var_storage.txt', 'x')
f = open('var_storage.txt', 'w')
f.write('0')

for i in range(repititions):
    html = driver.page_source   # Renders the JS and stores it as static HTML
    soup = BeautifulSoup(html, "html.parser")   # Sets the rendered JS to a Beautiful Soup object


    # No more website interaction is needed, so we can safely quit the driver
    driver.quit()

    # Finds every piece of content that has the class name of a posted listing
    activated_postings = soup.find_all(
        class_ = 'schedule-list-item active ng-star-inserted')

    # Checks if there are any more listings have been posted
    count = 0
    for posting in activated_postings:
        count += 1

    # Currently it's just using a text file to store how many listings were
    # posted last time. I may need a better solution like pickle.
    f = open('var_storage.txt', 'r')
    stored_number = f.read()
    f.close()

    # If there are more listings posted now then there were before than it
    # executes an AppleScript which sends a notification and then updates the
    # number.
    if stored_number <= count:
        send_notification = applescript.run('''display notification "New listings have been
        posted." with title "New Listings"''')
        file = open('var_storage.txt', 'w')
        file.write(stored_number)
        file.close()

    sleep(120)
    driver.refresh()

os.remove('var_storage.txt')
