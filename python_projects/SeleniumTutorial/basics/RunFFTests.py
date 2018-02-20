from selenium import webdriver

class RunFFTest():
    def test(self):
        #Instantiate FF browse
        driver =  webdriver.Firefox()

        #Open URL
        driver.get("https://letskodeit.com")
ff = RunFFTest()
ff.test()