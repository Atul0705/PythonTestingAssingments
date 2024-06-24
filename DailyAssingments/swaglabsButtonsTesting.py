import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class swaglabs:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def setup(self):

        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").clear()
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def logout(self):
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        self.driver.find_element(By.ID, "logout_sidebar_link").click()

    def endToEndTesting(self):
        buttons = self.driver.find_elements(By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory ']")
        for button in buttons:
            button.click()

        cartvalue = self.driver.find_element(By.XPATH, "//*[@data-test='shopping-cart-badge']").text
        try:
            assert cartvalue == "6"
        except AssertionError:
            print("Assertion failed not matching elements found in the cart")

        self.driver.find_element(By.XPATH, "//*[@data-test='shopping-cart-badge']").click()

        self.driver.find_element(By.ID, "checkout").click()
        try:
            self.driver.find_element(By.ID, "first-name").send_keys("xyz")
        except AssertionError:
            print("Not Able to insert details in first name")

        try:
            self.driver.find_element(By.ID, "last-name").send_keys("abc")
        except AssertionError:
            print("Assertion failed not able to enter lastname im the testbox")

        self.driver.find_element(By.ID, "postal-code").send_keys("100010")
        self.driver.find_element(By.ID, "continue").click()
        total = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        print(total)

        prodlist = self.driver.find_elements(By.XPATH, "//*[@class='inventory_item_name']")
        for products in prodlist:
            print(products.text)

        self.driver.find_element(By.ID, "finish").click()
        successmsg = self.driver.find_element(By.XPATH, "//h2").text
        print(successmsg)

    def fetchmsg(self):
        text = self.driver.find_element(By.TAG_NAME, "h3").text
        print(text)


sl = swaglabs()
sl.setup()
print("------------------------------------- Test 1 E2E Testing -------------------------------------------------------")
sl.login("standard_user", "secret_sauce")
sl.endToEndTesting()
sl.logout()
print("------------------------------------- Test 2 Locked out user -------------------------------------------------------")
sl.login("locked_out_user", "secret_sauce")
sl.fetchmsg()
# print("------------------------------------- Test 3  Problem user -------------------------------------------------------")
# sl.login("problem_user", "secret_sauce")
# sl.endToEndTesting()
print( "------------------------------------- Test 4 Performance glitch user-------------------------------------------------------")
sl.login("performance_glitch_user", "secret_sauce")
sl.endToEndTesting()
sl.logout()
print("------------------------------------- Test 5  Error user -------------------------------------------------------")
sl.login("error_user", "secret_sauce")
sl.endToEndTesting()
sl.teardown()
