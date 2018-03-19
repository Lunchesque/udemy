from selenium import webdriver
import time

class RunFFTest():
    def test(self):
        #Instantiate FF browse
        driver =  webdriver.Chrome()

        #Open URL
        driver.get("https://letskodeit.com")
        time.sleep(3)
ff = RunFFTest()
ff.test()
