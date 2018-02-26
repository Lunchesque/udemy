from selenium import webdriver
from utilities.handy_wrappers import HandyWrappers
from utilities.explicit_wait_type import ExplicitWaitType
from selenium.webdriver.common.action_chains import ActionChains

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

        ActionChains(driver).pause(2).perform()

ff = ExplicitWaitDemo2()
ff.test()