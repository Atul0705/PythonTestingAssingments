#Open http://demo.guru99.com/test/
#Then fill the date and print the conformation msg

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class datePicker:
    def DatePicker(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://demo.guru99.com/test/")
        date = driver.find_element(By.XPATH,"//*[@name='bdaytime']")
        date.send_keys("21072001")
        date.send_keys("0923PM")
        driver.find_element(By.XPATH,"//*[@type='submit']").click()
        wait = WebDriverWait(driver,10)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"div[style='font-size:15px;margin-left:50px;']")))
        print(driver.find_element(By.CSS_SELECTOR,"div[style='font-size:15px;margin-left:50px;']").text)

dp = datePicker()
dp.DatePicker()