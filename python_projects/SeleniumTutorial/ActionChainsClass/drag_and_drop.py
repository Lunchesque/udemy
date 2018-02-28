from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from utilities.handy_wrappers import HandyWrappers

class DragAndDrop():

    def dragAnddrop(self):
        baseUrl = "http://www.jqueryui.com/droppable/"
        driver = webdriver.Chrome()
        actions = ActionChains(driver)
        wrap = HandyWrappers(driver)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)

        driver.switch_to.frame(0)
        fromElement  = wrap.getElement("//body[1]/div[1]")
        toElement = wrap.getElement("//body/div[2]")
        ActionChains(driver).pause(2).perform()

        try:
            #actions.drag_and_drop(fromElement, toElement).perform()
            actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
            print("Drag And Drop Seccessful")
            ActionChains(driver).pause(2).perform()
        except:
            print("Drag And Drop FAILED")

ff = DragAndDrop()
ff.dragAnddrop()