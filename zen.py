# Import Selenium and relevant dependencies
import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import relative_locator as RL
from selenium.webdriver.support.relative_locator import locate_with

# Import browsers driver dependencies.
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

#  Added to silence certificate issuer warnings
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

optiona = webdriver.EdgeOptions()
optiona.add_experimental_option('excludeSwitches', ['enable-logging'])

class ZenTestCase(unittest.TestCase):
    """This class represents the Zen technical Assessment test case"""

    def setUp(self):
        """Define test variables, browser and initialize login variables."""

        print("======================================")
        print("===== Zen Assessment Test Start Here =====")
        print("======================================","\n")

        # Setting Other details
        ## Instantiating expected List values for Assertion
        self.exp_feat_list = ['Zero account opening balance', 'Internet Banking', 'Zenith Mobile Banking app', '*966# Eazybanking', 'MasterCard/Visa/Verve debit card', 'Email/SMS Alertz', 'Cheque book']
        self.exp_req_list = ['Account opening form duly completed', 'One recent clear passport photograph of signatory', 'Identification of signatories (Driver’s License, International Passport,\nNational Identity Card or Voter’s Card)', 'Residence permit (where applicable)', 'Two independent and satisfactory references', 'Public Utility Receipt dated within the last three months (PHCN bill, water rate bill, tenement rate, rent\nreceipt, telephone bill)']
        self.exp_chn_list = ['*966# EazyBanking', 'Zenith Internet Banking', 'In-branch at any Zenith Bank branch', 'ZenithDirect – our 24/7 telephone banking', 'Zenith Bank ATM nation-wide – free cash withdrawal', 'Zenith Mobile Banking App – 24/7 on your smart phone', 'Access your account using your Zenith Bank debit card at participating merchant stores for payment of goods and services in Nigeria and anywhere in the world']



    def tearDown(self):
        """Executed after reach test"""
        self.driverChrome.quit()
        self.driverEdge.quit()
        print("===Closing all browsers===")


    def test_current_account(self):
        print("===Testing current accounts on all browser===","\n")

        print("=================================")
        print("=====Testing Chrome browser======")
        print("=================================","\n")

        # Initialize browsers drivers
        self.driverChrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        # Request webpage loading
        self.driverChrome.get("https://www.zenithbank.com/")
        print("=== Opening Zen webpage on chrome browsers ===","\n")

        self.driverChrome.maximize_window()
        print("=== Maximize Chrome browser===","\n")

        # Initiate a driver wait to ensure cookie popup box loads before accepting
        popup_box = WebDriverWait(self.driverChrome, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Continue']")))


        #  Assert the popup box before using the Click function
        try:
            self.assertTrue (popup_box.is_displayed(), "Cookie popup element is not visible")
            print("=== Cookie Popup Assertion Successful ===","\n")
            popup_box.click()
        except AssertionError as e:
            print(f"Assertion failed: {e}")

        #time.sleep(5)

        # Creating wait to allow complete loading
        home_page = WebDriverWait(self.driverChrome, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='menu-main-menu-1']/li[2]/a/span")))

        #  Assert the Zenith homepage is successfully loaded.
        try:
            self.assertTrue (home_page.is_displayed(), "Zenith homepage wasn't loaded properly")
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
        actions = ActionChains(self.driverChrome)

        # Hover on the  personal banking link to show hover menu
        personal_bank = self.driverChrome.find_element(By.XPATH, "//*[@id='menu-main-menu-1']/li[2]/a/span")
        actions.move_to_element(personal_bank).perform()
        time.sleep(3)     # To allow visibility of actions

        #identify sub menu element - bank account
        bank_acct = self.driverChrome.find_element(By.XPATH, "//*[@id='menu-main-menu-1']/li[2]/ul/li[1]/a")
        actions.move_to_element(bank_acct).perform()
        time.sleep(3)

        #identify sub menu element - Currents Account
        curr_acc = self.driverChrome.find_element(By.XPATH, "//*[@id='menu-main-menu-1']/li[2]/ul/li[1]/ul/li[3]/a")
        actions.move_to_element(curr_acc).click().perform()

        # Creating wait to allow complete page loading
        home_page = WebDriverWait(self.driverChrome, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='1640']/section[2]/div/div/section/div/div[2]/div/section[1]/div/div/div/h1")))

        #  Assert the current accounts page is successfully loaded.
        try:
            self.assertTrue (home_page.is_displayed(), "Current Account wasn't loaded successfully/Click action not performed")
            print("=== Current Account Page Assertion Successful ===","\n")
        except AssertionError as e:
            print(f"Assertion failed: {e}")


        """
        Validating the  Features of the "individual Current Account"
        (Check the visibility of the features list and Feature link text is clickable)
        Validating the  Requirements of the "individual Current Account"
        (Check the visibility of the requirement list and requirement link text is clickable)
        Validating the Available Channels of the "individual Current Account"
        (Check the visibility of the Available Channels list and Available Channels link text is clickable)
        """


        time.sleep(3)

        # Get the relative position of the Individual Current Account section
        ind_curr_acc = self.driverChrome.find_element(By.XPATH, "//*[@id='1640']/section[2]/div/div/section/div/div[2]/div/section[1]/div/div/div/h1")


        """
        Validating the features on  Individual current account
        using relative locator functiom since other account types sections
        uses same CSS selector values
        """

        # View the contents of the features list by click action
        ind_el = self.driverChrome.find_element(locate_with(By.CSS_SELECTOR, "#\#features-and-benefits").below(ind_curr_acc))
        ind_el.click()

        # Creating wait to allow action visibility
        feat_list = WebDriverWait(self.driverChrome, 3).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='ui-id-2']/section/div/div/div/ul/li[1]")))

        #  Assert the feature and benefit link respond to click.
        try:
            self.assertTrue (feat_list.is_displayed(), "Feature list is not visible/Click action not performed")
            print("=== Individual Current Account Features Clickable Assertion Successful ===","\n")
        except AssertionError as e:
            print(f"Assertion failed: {e}")


        # Check the  availability of the features lists on the page

        my_feat =  self.driverChrome.find_element(locate_with(By.XPATH, "//*[@id='ui-id-2']/section/div/div/div/ul").below(ind_el))
        list_feat = my_feat.find_elements(By.XPATH, "./li")
        self.act_list_feat = [my_val.text for my_val in list_feat]
        #print(act_list_feat)


        #  Assert the features list on the page is same as the expected features list.
        try:
            self.assertListEqual (self.act_list_feat, self.exp_feat_list, "Feature list is not same as Expected")
            print("=== Individual Current Account Features List Assertion Successful ===","\n")
        except AssertionError as e:
            print(f"Assertion failed: {e}")



        """
        Validating the requirement details on  Individual current account
        using relative locator functiom since other account types sections
        uses same CSS selector values
        """

        # View the contents of the requirement list by click action
        ind_req = self.driverChrome.find_element(locate_with(By.CSS_SELECTOR, "#\#requirements").below(ind_curr_acc))
        ind_req.click()

        # Creating wait to allow action visibility
        req_list = WebDriverWait(self.driverChrome, 3).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='ui-id-4']/section/div/div/div/ul/li[1]")))

        #  Assert the requirements link respond to click.
        try:
            self.assertTrue (req_list.is_displayed(), "Requirements list is not visible/Click action not performed")
            print("=== Individual Current Account Requirements Clickable Assertion Successful ===","\n")
        except AssertionError as e:
            print(f"Assertion failed: {e}")


        # Check the  availability of the requirements lists on the page

        my_reqs =  self.driverChrome.find_element(locate_with(By.XPATH, "//*[@id='ui-id-4']/section/div/div/div/ul").below(ind_el))
        list_req = my_reqs.find_elements(By.XPATH, "./li")
        self.act_list_req = [my_req.text for my_req in list_req]



        #  Assert the requirements list on the page is same as the expected requirement list.
        try:
            self.assertListEqual (self.act_list_req, self.exp_req_list, "Requirements list is not same as Expected")
            print("=== Individual Current Account Requirements List Assertion Successful ===","\n")
        except AssertionError as e:
            print(f"Assertion failed: {e}")



        """
        Validating the Available channel details on Individual current account
        using relative locator functiom since other account types sections
        uses same CSS selector values
        """

        # View the contents of the Available channels list by click action
        ind_chn = self.driverChrome.find_element(locate_with(By.CSS_SELECTOR, "#\#available-channels").below(ind_curr_acc))
        ind_chn.click()

        # Creating wait to allow action visibility
        chn_list = WebDriverWait(self.driverChrome, 3).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='ui-id-6']/section/div/div/div/ul/li[1]")))

        #  Assert the available channels link respond to click.
        try:
            self.assertTrue (chn_list.is_displayed(), "Available Channels list is not visible/Click action not performed")
            print("=== Individual Current Account Available Channel Clickable Assertion Successful ===","\n")
        except AssertionError as e:
            print(f"Assertion failed: {e}")


        # Check the  availability of the requirements lists on the page

        my_chans =  self.driverChrome.find_element(locate_with(By.XPATH, "//*[@id='ui-id-6']/section/div/div/div/ul").below(ind_el))
        list_chn = my_chans.find_elements(By.XPATH, "./li")
        self.act_list_chn = [my_chn.text for my_chn in list_chn]


        #  Assert the requirements list on the page is same as the expected requirement list.
        try:
            self.assertListEqual (self.act_list_chn, self.exp_chn_list, "Available Channels list is not same as Expected")
            print("=== Individual Current Account Available Channel List Assertion Successful ===","\n")
        except AssertionError as e:
            print(f"Assertion failed: {e}")


        print("=================================")
        print("=====Testing EDGE browser======")
        print("=================================","\n")
        
        # Initialize browsers drivers
        self.driverEdge = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=optiona)

        # Request webpage loading
        self.driverEdge.get("https://www.zenithbank.com/")
        print("=== Opening Zen webpage on Edge browsers ===","\n")
        
        self.driverEdge.maximize_window()
        print("=== Maximize Edge browser===","\n")

        # Initiate a driver wait to ensure cookie popup box loads before accepting
        popup_box = WebDriverWait(self.driverEdge, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Continue']")))


        #  Assert the popup box before using the Click function
        try:
            self.assertTrue (popup_box.is_displayed(), "Cookie popup element is not visible")
            print("=== Cookie Popup Assertion Successful ===","\n")
            popup_box.click()
        except AssertionError as e:
            print(f"Assertion failed: {e}")

        #time.sleep(5)

        # Creating wait to allow complete loading
        home_page = WebDriverWait(self.driverEdge, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='menu-main-menu-1']/li[2]/a/span")))

        #  Assert the Zenith homepage is successfully loaded.
        try:
            self.assertTrue (home_page.is_displayed(), "Zenith homepage wasn't loaded properly")
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
        actions = ActionChains(self.driverEdge)

        # Hover on the  personal banking link to show hover menu
        personal_bank = self.driverEdge.find_element(By.XPATH, "//*[@id='menu-main-menu-1']/li[2]/a/span")
        actions.move_to_element(personal_bank).perform()
        time.sleep(3)     # To allow visibility of actions

        #identify sub menu element - bank account
        bank_acct = self.driverEdge.find_element(By.XPATH, "//*[@id='menu-main-menu-1']/li[2]/ul/li[1]/a")
        actions.move_to_element(bank_acct).perform()
        time.sleep(3)

        #identify sub menu element - Currents Account
        curr_acc = self.driverEdge.find_element(By.XPATH, "//*[@id='menu-main-menu-1']/li[2]/ul/li[1]/ul/li[3]/a")
        actions.move_to_element(curr_acc).click().perform()

        # Creating wait to allow complete page loading
        home_page = WebDriverWait(self.driverEdge, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='1640']/section[2]/div/div/section/div/div[2]/div/section[1]/div/div/div/h1")))

        #  Assert the current accounts page is successfully loaded.
        try:
            self.assertTrue (home_page.is_displayed(), "Current Account wasn't loaded successfully/Click action not performed")
            print("=== Current Account Page Assertion Successful ===","\n")
        except AssertionError as e:
            print(f"Assertion failed: {e}")


        """
        Validating the  Features of the "individual Current Account"
        (Check the visibility of the features list and Feature link text is clickable)
        Validating the  Requirements of the "individual Current Account"
        (Check the visibility of the requirement list and requirement link text is clickable)
        Validating the Available Channels of the "individual Current Account"
        (Check the visibility of the Available Channels list and Available Channels link text is clickable)
        """


        time.sleep(3)

        # Get the relative position of the Individual Current Account section
        ind_curr_acc = self.driverEdge.find_element(By.XPATH, "//*[@id='1640']/section[2]/div/div/section/div/div[2]/div/section[1]/div/div/div/h1")


        """
        Validating the features on  Individual current account
        using relative locator functiom since other account types sections
        uses same CSS selector values
        """

        # View the contents of the features list by click action
        ind_el = self.driverEdge.find_element(locate_with(By.CSS_SELECTOR, "#\#features-and-benefits").below(ind_curr_acc))
        ind_el.click()

        # Creating wait to allow action visibility
        feat_list = WebDriverWait(self.driverEdge, 3).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='ui-id-2']/section/div/div/div/ul/li[1]")))

        #  Assert the feature and benefit link respond to click.
        try:
            self.assertTrue (feat_list.is_displayed(), "Feature list is not visible/Click action not performed")
            print("=== Individual Current Account Features Clickable Assertion Successful ===","\n")
        except AssertionError as e:
            print(f"Assertion failed: {e}")


        # Check the  availability of the features lists on the page

        my_feat =  self.driverEdge.find_element(locate_with(By.XPATH, "//*[@id='ui-id-2']/section/div/div/div/ul").below(ind_el))
        list_feat = my_feat.find_elements(By.XPATH, "./li")
        self.act_list_feat = [my_val.text for my_val in list_feat]
        #print(act_list_feat)


        #  Assert the features list on the page is same as the expected features list.
        try:
            self.assertListEqual (self.act_list_feat, self.exp_feat_list, "Feature list is not same as Expected")
            print("=== Individual Current Account Features List Assertion Successful ===","\n")
        except AssertionError as e:
            print(f"Assertion failed: {e}")



        """
        Validating the requirement details on  Individual current account
        using relative locator functiom since other account types sections
        uses same CSS selector values
        """

        # View the contents of the requirement list by click action
        ind_req = self.driverEdge.find_element(locate_with(By.CSS_SELECTOR, "#\#requirements").below(ind_curr_acc))
        ind_req.click()

        # Creating wait to allow action visibility
        req_list = WebDriverWait(self.driverEdge, 3).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='ui-id-4']/section/div/div/div/ul/li[1]")))

        #  Assert the requirements link respond to click.
        try:
            self.assertTrue (req_list.is_displayed(), "Requirements list is not visible/Click action not performed")
            print("=== Individual Current Account Requirements Clickable Assertion Successful ===","\n")
        except AssertionError as e:
            print(f"Assertion failed: {e}")


        # Check the  availability of the requirements lists on the page

        my_reqs =  self.driverEdge.find_element(locate_with(By.XPATH, "//*[@id='ui-id-4']/section/div/div/div/ul").below(ind_el))
        list_req = my_reqs.find_elements(By.XPATH, "./li")
        self.act_list_req = [my_req.text for my_req in list_req]



        #  Assert the requirements list on the page is same as the expected requirement list.
        try:
            self.assertListEqual (self.act_list_req, self.exp_req_list, "Requirements list is not same as Expected")
            print("=== Individual Current Account Requirements List Assertion Successful ===","\n")
        except AssertionError as e:
            print(f"Assertion failed: {e}")



        """
        Validating the Available channel details on Individual current account
        using relative locator functiom since other account types sections
        uses same CSS selector values
        """

        # View the contents of the Available channels list by click action
        ind_chn = self.driverEdge.find_element(locate_with(By.CSS_SELECTOR, "#\#available-channels").below(ind_curr_acc))
        ind_chn.click()

        # Creating wait to allow action visibility
        chn_list = WebDriverWait(self.driverEdge, 3).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='ui-id-6']/section/div/div/div/ul/li[1]")))

        #  Assert the available channels link respond to click.
        try:
            self.assertTrue (chn_list.is_displayed(), "Available Channels list is not visible/Click action not performed")
            print("=== Individual Current Account Available Channel Clickable Assertion Successful ===","\n")
        except AssertionError as e:
            print(f"Assertion failed: {e}")


        # Check the  availability of the requirements lists on the page

        my_chans =  self.driverEdge.find_element(locate_with(By.XPATH, "//*[@id='ui-id-6']/section/div/div/div/ul").below(ind_el))
        list_chn = my_chans.find_elements(By.XPATH, "./li")
        self.act_list_chn = [my_chn.text for my_chn in list_chn]


        #  Assert the requirements list on the page is same as the expected requirement list.
        try:
            self.assertListEqual (self.act_list_chn, self.exp_chn_list, "Available Channels list is not same as Expected")
            print("=== Individual Current Account Available Channel List Assertion Successful ===","\n")
        except AssertionError as e:
            print(f"Assertion failed: {e}")

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
