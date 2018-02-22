from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class HiddenElements():

    def testLetsKodeIt(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)

        # Find the state of the text box
        textBoxElement = driver.find_element(By.ID, "displayed-text")
        textBoxState = textBoxElement.is_displayed() # True if visible, False if hidden
        # Exception if not present in the DOM
        print("Text is visible? " + str(textBoxState))
        ActionChains(driver).pause(2).perform()

        # Click the Hide button
        driver.find_element(By.ID, "hide-textbox").click()
        # Find the state of the text box
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible? " + str(textBoxState))
        ActionChains(driver).pause(2).perform()

        driver.find_element(By.ID, "show-textbox").click()
        # Find the state of the text box
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible? " + str(textBoxState))
        ActionChains(driver).pause(2).perform()
        # Browser Close
        driver.quit()

    def testExpedia(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        driver.find_element(By.ID, "tab-flight-tab-hp").click()

        drpdwnElement = driver.find_element(By.ID, "flight-age-select-1-hp-flight")
        print("Element visible? " + str(drpdwnElement.is_displayed()))


ff = HiddenElements()
ff.testLetsKodeIt()
ff.testExpedia()