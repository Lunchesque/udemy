from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from MyCaseWithHandyWrappers import HandyWrappers

class ElPresenceCheck():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        wrapper = HandyWrappers(driver)
        driver.get(baseUrl)

        elementResult1 = wrapper.isElementPresent("//input[@id='name']", By.XPATH)
        print(str(elementResult1))

        elementResult2 = wrapper.elementPresenceCheck("name", By.ID)
        print(str(elementResult2))

ff = ElPresenceCheck()
ff.test()