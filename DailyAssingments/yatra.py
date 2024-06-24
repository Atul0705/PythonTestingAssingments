import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Yatra:
    def verify_Contact_Us(self):
        driver = webdriver.Chrome()

        #adding global wait
        driver.implicitly_wait(5)
        driver.maximize_window()

        #opening yatra.com
        driver.get("https://www.yatra.com/")
        print(driver.title)
        driver.find_element(By.XPATH, "//span[@class='more-arr']").click()
        # storing the elements and performing click on adventures
        listName = driver.find_elements(By.CSS_SELECTOR, ".moreOption li a")
        for element in listName:
            if element.text == "Adventures":
                element.click()
                break
        #opening gear tab
        driver.find_element(By.XPATH, "//li[@class='gearLink']//span[contains(text(),'Gear')]").click()
        time.sleep(1)
        handles = driver.window_handles

        #switching to new opened tab/window
        driver.switch_to.window(handles[1])
        print(driver.title)


        #wait until search box is located
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "(//input[@placeholder='Search'])[2]")))
        driver.close()


yatra = Yatra()
yatra.verify_Contact_Us()
