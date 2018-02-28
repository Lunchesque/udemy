from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from utilities.handy_wrappers import HandyWrappers

class Mousehover():

    def mouseHover(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice/"
        driver = webdriver.Chrome()
        wrap = HandyWrappers(driver)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)

        driver.execute_script("window.scrollBy(0, 600);")
        hoverElement = wrap.getElement("//button[@id='mousehover']")
        ActionChains(driver).move_to_element(hoverElement).perform()
        print("Moved mouse to MOUSE HOVER button")
        ActionChains(driver).pause(2).perform()

        topBtn = wrap.getElement("//a[@href='#top']")
        ActionChains(driver).move_to_element(topBtn).click().perform()
        print("Clicked TOP on MOUSE HOVER DROPDOWN")
        ActionChains(driver).pause(2).perform()

        driver.execute_script("window.scrollBy(0, 600);")
        ActionChains(driver).move_to_element(hoverElement).perform()
        print("Moved mouse to MOUSE HOVER button AGAIN")
        ActionChains(driver).pause(2).perform()

        reloadBtn = wrap.getElement("//a[text()='Reload']")
        ActionChains(driver).move_to_element(reloadBtn).click().perform()
        print("Clicked RELOAD on MOUSE HOVER DROPDOWN")
        ActionChains(driver).pause(3).perform()

ff = Mousehover()
ff.mouseHover()