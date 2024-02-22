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
    print("=== Cookie Popup Assertion Successful===","\n")
    popup_box.click()
except AssertionError as e:
    print(f"Assertion failed: {e}")

#time.sleep(5)


page_load = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='menu-main-menu-1']/li[2]/a/span")))

#  Assert the Zenith homepage is successfully loaded.
try:
    assert page_load.is_displayed(), "Zenith homepage wasn't loaded properly"
    print("=== Zenith Homepage Assertion Successful===","\n")
except AssertionError as e:
    print(f"Assertion failed: {e}")

"""
Apply Actionchain to hover on the personal
"""