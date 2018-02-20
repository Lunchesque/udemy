from selenium import webdriver

class RunChromeTest():
    def test(self):
        #Instantiate FF browse
        driver =  webdriver.Chrome()

        #Open URL
        driver.get("https://letskodeit.com")
ff = RunChromeTest()
ff.test()