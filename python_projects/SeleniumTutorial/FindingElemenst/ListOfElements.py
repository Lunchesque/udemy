from selenium import webdriver
from selenium.webdriver.common.by import By

class ListOfElements():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)

        elementListByClassName = driver.find_elements(By.CLASS_NAME, "inputs")
        length1 = len(elementListByClassName)

        if elementListByClassName is not None:
            print("Size of the list BY CLASS NAME is: " + str(length1))

        elementListByTagName = driver.find_elements(By.TAG_NAME, "input")
        length2 = len(elementListByTagName)

        if elementListByTagName is not  None:
            print("Size of the list BY TAG NAME is: " + str(length2))

ff = ListOfElements()
ff.test()