from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

class DropdownSelect():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        element = driver.find_element(By.ID, "carselect")
        sel = Select(element)

        sel.select_by_value("benz")
        print("Select BENZ by value")
        ActionChains(driver).pause(2).perform()

        sel.select_by_index(2)
        print("Select HONDA by index")
        ActionChains(driver).pause(2).perform()

        sel.select_by_visible_text("BMW")
        print("Select BMW by visible text")
        ActionChains(driver).pause(2).perform()

        sel.select_by_index("2")
        print("Another way to select by INDEX")
        ActionChains(driver).pause(2).perform()


ff = DropdownSelect()
ff.test()