import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Flipkart:

    def andriod_Phones(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.maximize_window()
        #opeining flipkart
        driver.get("https://www.flipkart.com/")

        #search bar
        driver.find_element(By.XPATH, "//*[@placeholder='Search for Products, Brands and More']").send_keys("all Android mobile")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()

        #sorting the price to low to high
        driver.find_element(By.XPATH,"d").click()
        time.sleep(1)
        #printing the first product price and name
        name = driver.find_element(By.XPATH,"(//*[@class='_4rR01T'])[1]")
        print(name.text)
        print(driver.find_element(By.XPATH,"(//*[@class='_30jeq3 _1_WHN1'])[1]").text)


ff = Flipkart()
ff.andriod_Phones()