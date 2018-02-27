from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from utilities.handy_wrappers import HandyWrappers
from utilities.screenshots_generic import TakeScreenshot

class Screenshots():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com"
        snap = TakeScreenshot()
        driver = webdriver.Chrome()
        driver.maximize_window()
        wrapper = HandyWrappers(driver)
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        wrapper.getElement("//a[@href='/sign_in']").click()
        wrapper.getElement("//input[@id='user_email']").send_keys("abc@email.com")
        wrapper.getElement("//input[@id='user_password']").send_keys("abc")
        wrapper.getElement("//input[@type='submit']").click()
        snap.takeScreenshot(driver)
        ActionChains(driver).pause(2).perform()

ff = Screenshots()
ff.test()