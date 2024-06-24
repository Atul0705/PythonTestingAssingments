from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class dragAndDrop:
    def dragNdDrop(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        url = "https://demo.guru99.com/test/drag_drop.html"
        driver.get(url)

        # Performing drag and drop using action class
        # locate the target element and destination element
        source = driver.find_element(By.XPATH, "//*[@id='credit2']")
        destination = driver.find_element(By.XPATH, "//*[@id='bank']/li")

        act = ActionChains(driver)

        act.drag_and_drop(source, destination)
        driver.get_screenshot_as_file("screenshot.png")

        driver.quit()


dd = dragAndDrop()
dd.dragNdDrop()
