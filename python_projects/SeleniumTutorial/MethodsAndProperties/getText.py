from selenium import webdriver
from selenium.webdriver.common.by import By


class GetText():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)

        openTabElement = driver.find_element(By.ID, "opentab")
        texOpenTab = openTabElement.text

        if texOpenTab == "Open Tab":
            print(texOpenTab)


ff = GetText()
ff.test()