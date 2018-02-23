from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class GetAttribute():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)

        element1 = driver.find_element(By.ID, "name")
        attr1 = element1.get_attribute("placeholder")
        print(str(attr1))

        ActionChains(driver).pause(2).perform()

        element2 = driver.find_element(By.XPATH, "//button[@id='mousehover']")
        attr2 = element2.get_attribute("class")
        print(str(attr2))

ff = GetAttribute()
ff.test()