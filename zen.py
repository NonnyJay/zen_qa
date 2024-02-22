# Import Selenium and relevant dependencies

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support import relative_locator as RL
from selenium.webdriver.support.relative_locator import locate_with


from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


#  Added to silence certificate issuer warnings
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# Initialize browsers drivers
driver.get("https://www.zenithbank.com/")
driver.maximize_window()

# Initiate a driver wait to ensure cookie popup box loads before accepting
popup_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Continue']")))


#  Assert the popup box before using the Click function
try:
    assert popup_box.is_displayed(), "Cookie popup element is not visible"
    print("=== Cookie Popup Assertion Successful ===","\n")
    popup_box.click()
except AssertionError as e:
    print(f"Assertion failed: {e}")

#time.sleep(5)

# Creating wait to allow complete loading
home_page = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='menu-main-menu-1']/li[2]/a/span")))

#  Assert the Zenith homepage is successfully loaded.
try:
    assert home_page.is_displayed(), "Zenith homepage wasn't loaded properly"
    print("=== Zenith Homepage Assertion Successful ===","\n")
except AssertionError as e:
    print(f"Assertion failed: {e}")

"""
Apply Actionchain to hover on the personal Menu
Select the "Bank Accouts
Select the "Current Accounts"
Sleep time was applied to allow visibility of these actions
"""

#Setup Action Chain
actions = ActionChains(driver)

# Hover on the  personal banking link to show hover menu
personal_bank = driver.find_element(By.XPATH, "//*[@id='menu-main-menu-1']/li[2]/a/span")
actions.move_to_element(personal_bank).perform()
time.sleep(3)     # To allow visibility of actions

#identify sub menu element - bank account
bank_acct = driver.find_element(By.XPATH, "//*[@id='menu-main-menu-1']/li[2]/ul/li[1]/a")
actions.move_to_element(bank_acct).perform()
time.sleep(3)

#identify sub menu element - Currents Account
curr_acc = driver.find_element(By.XPATH, "//*[@id='menu-main-menu-1']/li[2]/ul/li[1]/ul/li[3]/a")
actions.move_to_element(curr_acc).click().perform()

# Creating wait to allow complete page loading
home_page = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='1640']/section[2]/div/div/section/div/div[2]/div/section[1]/div/div/div/h1")))

#  Assert the current accounts page is successfully loaded.
try:
    assert home_page.is_displayed(), "Current Account wasn't loaded successfully/Click action not performed"
    print("=== Current Account Page Assertion Successful ===","\n")
except AssertionError as e:
    print(f"Assertion failed: {e}")

time.sleep(10)