from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class WorkingWithElementsList():

    def testListOfElements(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        radioButtonsList = driver.find_elements(By.XPATH, "//input[@type='radio']")
        size = len(radioButtonsList)
        print("Size of the list of radio buttons: " + str(size))

        for radioButton in radioButtonsList:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                ActionChains(driver).pause(1).perform()

ff = WorkingWithElementsList()
ff.testListOfElements()