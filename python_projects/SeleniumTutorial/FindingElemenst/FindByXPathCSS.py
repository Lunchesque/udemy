from selenium import webdriver

class FindByXPathCSS():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        elementByXpath = driver.find_element_by_xpath("//input[@id='name']")
        elementByCSS = driver.find_element_by_css_selector("#displayed-text")

        if elementByXpath is not None:
            print("We found an element by XPATH")

        if elementByCSS is not None:
            print("We found an element by CSS")

ff = FindByXPathCSS()
ff.test()