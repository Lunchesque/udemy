from selenium import webdriver
from selenium.webdriver.common.by import By

class ClickAndSendKeys():

    def test(self):
        baseUrl = ""https://letskodeit.teachable.com/p/practice""
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)

        driver.find_element(By.XPATH)