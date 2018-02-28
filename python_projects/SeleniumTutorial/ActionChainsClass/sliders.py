from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from utilities.handy_wrappers import HandyWrappers

class Sleders():

    def sliders(self):
        baseUrl = "http://jqueryui.com/slider/"
        driver = webdriver.Chrome()
        wrap = HandyWrappers(driver)
        actions = ActionChains(driver)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)

        driver.switch_to.frame(0)
        sliderElement = wrap.getElement("//div[@id='slider']/span")
        actions.pause(2).perform()
        try:
            actions.drag_and_drop_by_offset(sliderElement, 150, 0)
            print("Slided!")
            actions.pause(2).perform()
        except:
            print("Sliding Failed")

ff = Sleders()
ff.sliders()