from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ClickAndSendKeys():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        login = driver.find_element(By.XPATH, "//a[@href='/sign_in']")
        login.click()

        email = driver.find_element(By.ID, "user_email")
        email.send_keys("test")
        password = driver.find_element(By.ID, "user_password")
        password.send_keys("test")

        ActionChains(driver).pause(3).perform()

        email.clear()
        password.clear()

        ActionChains(driver).pause(3).perform()

        email.send_keys("TEST")
        password.send_keys("TEST")

        ActionChains(driver).pause(3).perform()

ff = ClickAndSendKeys()
ff.test()