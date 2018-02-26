from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from utilities.handy_wrappers import HandyWrappers

class MyCaseWithHandyWrappers():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        wrapper = HandyWrappers(driver)
        driver.implicitly_wait(5)
        driver.get(baseUrl)

        hideShow = wrapper.getElement("//input[@id='displayed-text']")
        hideShow.send_keys("TEXT")
        ActionChains(driver).pause(2).perform()

        hideBtn = wrapper.getElement("//input[@id='hide-textbox']")
        hideBtn.click()
        ActionChains(driver).pause(2).perform()

        showBtn = wrapper.getElement("//input[@id='show-textbox']")
        showBtn.click()
        ActionChains(driver).pause(1).perform()

ff = MyCaseWithHandyWrappers()
ff.test()