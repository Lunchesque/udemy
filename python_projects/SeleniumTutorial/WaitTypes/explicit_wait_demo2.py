from selenium import webdriver
from WaitTypes.explicit_wait_type import ExplicitWaitType
from utilities.handy_wrappers import HandyWrappers

class ExplicitWaitDemo2():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        wrapper = HandyWrappers(driver)
        wait = ExplicitWaitType(driver)
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(baseUrl)

        el = wrapper.getElement("//input[@id='displayed-text']")
        el.clear()
        el.send_keys("text")

        hideBtn = wrapper.getElement("//input[@id='hide-textbox']")
        hideBtn.click()

        showBtn = wrapper.getElement("//input[@id='show-textbox']")
        showBtn.click()

        element = wait.waitForElement("//input[@id='displayed-text']")
        element.click()

ff = ExplicitWaitDemo2()
ff.test()