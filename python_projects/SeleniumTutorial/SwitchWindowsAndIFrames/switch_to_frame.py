from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from utilities.handy_wrappers import HandyWrappers

class SwitchFrames():

    def switchFrames(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        wrap = HandyWrappers(driver)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)
        driver.execute_script("window.scrollBy(0, 1000);")

        #Swith to frame usind ID
        #driver.switch_to.frame("courses-iframe")

        #Swith to frame using name
        #driver.switch_to.frame("iframe-name")

        #Switch to frame using numbers
        driver.switch_to.frame(0)

        #Serch cource
        ActionChains(driver).pause(2).perform()
        wrap.getElement("//input[@id='search-courses']").send_keys("python")
        wrap.getElement("//button[@id='search-course-button']").click()
        ActionChains(driver).pause(2).perform()

        #Switch back to the parent handle
        driver.switch_to.default_content()
        wrap.getElement("//input[@id='name']").send_keys("ON THE MAIN FRAME")
        ActionChains(driver).pause(2).perform()

ff = SwitchFrames()
ff.switchFrames()