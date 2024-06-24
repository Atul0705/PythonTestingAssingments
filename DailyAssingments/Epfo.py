# Open epfo site
#capture the popup and print the text written on popup

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class ProvidentFund:
    def pf(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get("https://unifiedportal-mem.epfindia.gov.in/memberinterface/")
        time.sleep(2)
        msg = driver.find_elements(By.XPATH, "//div[@class='col-md-8']/div/span")
        for i in msg:
            print(i.text)

        driver.find_element(By.CSS_SELECTOR, "#btnCloseModal").click()

        driver.close()


pp = ProvidentFund()
pp.pf()
