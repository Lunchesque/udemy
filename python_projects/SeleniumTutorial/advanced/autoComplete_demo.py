from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from utilities.handy_wrappers import HandyWrappers

class AutoComplete():

    def test(self):
        baseUrl = "http://www.google.com"
        driver = webdriver.Chrome()
        wrapper = HandyWrappers(driver)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)

        wrapper.getElement("//input[@id='lst-ib']").send_keys("pyth")
        ActionChains(driver).pause(2).perform()
        wrapper.getElement("//ul[@role='listbox']//li[2]").click()

ff = AutoComplete()
ff.test()