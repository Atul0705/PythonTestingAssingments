import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class olx:
    def User_Email_Test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.olx.in")
        driver.find_element(By.CSS_SELECTOR, "[data-aut-id='btnLogin']").click()

        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "[data-aut-id='emailLogin']")))
        driver.find_element(By.CSS_SELECTOR, "[data-aut-id='emailLogin']").click()
        driver.find_element(By.ID,"email_input_field").send_keys("emailxxxxx@testxxx.com")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "[data-aut-id='submitBtn']").click()
        time.sleep(1)
        try:
            msg = driver.find_element(By.CSS_SELECTOR,".QjCQw").text
            print(msg)

        finally:
            print("NO POPUP FOUND")

        driver.quit()

olx = olx()
olx.User_Email_Test()