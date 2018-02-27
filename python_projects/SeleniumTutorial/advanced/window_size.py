from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class WindowSize():

    def getWindowSize(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)

        size = driver.get_window_size()
        print(size)
        height = driver.execute_script("return window.innerHeight;")
        print(str(height))
        width = driver.execute_script("return window.innerWidth;")
        print(str(width))
        #scroll down
        driver.execute_script("window.scrollBy(0, 1000);")
        ActionChains(driver).pause(2).perform()
        #scroll up
        driver.execute_script("window.scrollBy(0, -1000);")
        ActionChains(driver).pause(2).perform()
        #scroll element into view
        element = driver.find_element(By.XPATH, "//legend[contains(text(),'iFrame Example')]")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        ActionChains(driver).pause(2).perform()
        #Native way to scroll element into view
        driver.execute_script("window.scrollBy(0, -1000);")
        location = element.location_once_scrolled_into_view
        print(str(location))
        ActionChains(driver).pause(2).perform()

ff = WindowSize()
ff.getWindowSize()