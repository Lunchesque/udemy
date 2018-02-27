from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from utilities.handy_wrappers import HandyWrappers

class JavaScriptExecution():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        wrap = HandyWrappers(driver)
        driver.implicitly_wait(5)
        #driver.get(baseUrl)
        driver.execute_script("window.location = 'https://letskodeit.teachable.com/p/practice';")

        #element = wrap.getElement("//input[@id='name']")
        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("Test")

        ActionChains(driver).pause(3).perform()

ff = JavaScriptExecution()
ff.test()