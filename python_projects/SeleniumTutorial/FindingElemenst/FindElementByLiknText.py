from selenium import webdriver

class FindByLinkText():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        elementByLinkText = driver.find_element_by_link_text("Practice")
        elementByPartialLinkText = driver.find_element_by_partial_link_text("Logi")
        if elementByLinkText is not None:
            print("We found an element by Link Text")

        if elementByPartialLinkText is not  None:
            print("We found an element by Partial Link text")

ff = FindByLinkText()
ff.test()