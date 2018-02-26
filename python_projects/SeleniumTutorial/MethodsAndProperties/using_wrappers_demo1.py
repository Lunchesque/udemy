from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from utilities.handy_wrappers import HandyWrappers

class UsingWrappers():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        hw = HandyWrappers(driver)

        driver.get(baseUrl)

        textField1 = hw.getElement("name", "id")
        textField1.send_keys("Text")
        ActionChains(driver).pause(2).perform()

        textField2 = hw.getElement("//input[@id='name']")
        textField2.clear()
        ActionChains(driver).pause(1).perform()
        textField2.send_keys("NEW TEXT")
        ActionChains(driver).pause(2).perform()

ff = UsingWrappers()
ff.test()