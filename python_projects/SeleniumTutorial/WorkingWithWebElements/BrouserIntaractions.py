from selenium import webdriver

class BrowserInteractions():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()

        #Window maximize
        driver.maximize_window()
        print("We maximized the browser window")
        #Open the URL
        driver.get(baseUrl)
        print("We opened our 'baseUrl'")
        #Get title
        title = driver.title
        print("Title of the page is: " + title)
        #Get current URL
        URL = driver.current_url
        print("Current URL of the page is: " + URL)
        #Browser refresh
        driver.refresh()
        print("Browser refreshed FIRST time")

        driver.get(driver.current_url)
        print("Browser refreshed SECOND time")
        #Open another url
        driver.get("https://www.python.org")
        #Browser back
        driver.back()
        print("Go one step BACK in browser history")
        #Brouser forward
        driver.forward()
        print("Go one step FORWARD in browser history")
        #Get page source
        driver.page_source
        print("We get the page source")
        #Browser Close/Quit
        driver.quit()
        #driver.close()

ff = BrowserInteractions()
ff.test()