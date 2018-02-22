from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class RadioButtonsAndCheckboxes():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        bmwRadioBtn = driver.find_element(By.ID, "bmwradio")
        bmwRadioBtn.click()

        ActionChains(driver).pause(2).perform()

        benzRadioBtn = driver.find_element(By.ID, "benzradio")
        benzRadioBtn.click()

        ActionChains(driver).pause(2).perform()

        hondaRadioBtn =driver.find_element(By.ID, "hondaradio")
        hondaRadioBtn.click()

        ActionChains(driver).pause(2).perform()

        bmwCheckbox = driver.find_element(By.ID, "bmwcheck")
        bmwCheckbox.click()

        ActionChains(driver).pause(2).perform()

        benzCheckbox = driver.find_element(By.ID, "benzcheck")
        benzCheckbox.click()

        ActionChains(driver).pause(2).perform()

        print("BMW radio batton is selected? " + str(bmwRadioBtn.is_selected()))
        print("BENZ radio batton is selected? " + str(benzRadioBtn.is_selected()))
        print("HONDA radio batton is selected? " + str(hondaRadioBtn.is_selected()))
        print("BMW checkbox is selected? " + str(bmwCheckbox.is_selected()))
        print("BENZ checkbox is selected? " + str(benzCheckbox.is_selected()))

ff = RadioButtonsAndCheckboxes()
ff.test()