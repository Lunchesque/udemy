from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from utilities.handy_wrappers import HandyWrappers

class SwitchWindow():

    def switchWindow(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        wrap = HandyWrappers(driver)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)

        #Find parent window handle
        parentHandle = driver.current_window_handle
        print("Parent handle" + parentHandle)

        #find window btn and click it
        wrap.getElement("//button[@id='openwindow']").click()
        ActionChains(driver).pause(2).perform()

        #Find all handles
        handles = driver.window_handles

        #Switch to window and serch
        for handle in handles:
            print("Handle: " + handle)
            if  handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Switched to the window " + handle)
                searchBox  = wrap.getElement("//input[@id='search-courses']")
                searchBox.send_keys("python")
                wrap.getElement("//button[@id='search-course-button']").click()
                ActionChains(driver).pause(2).perform()
                driver.close()
                break

        #Switch back to parent handle
        driver.switch_to.window(parentHandle)
        wrap.getElement("//input[@id='name']").send_keys("On Main Window")
        ActionChains(driver).pause(3).perform()

ff = SwitchWindow()
ff.switchWindow()