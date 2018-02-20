from selenium import webdriver

class FindByLinkText():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        elementByClassName = driver.find_element_by_class_name("inputs")
        elementByClassName.send_keys("Test")

        if elementByClassName is not None:
            print("We found an element by Class Name")

        elementByTagName = driver.find_element_by_tag_name("a")
        elementByTagName.send_keys("Test")

        if elementByTagName is not  None:
            print("We found an element by Tag Name")

ff = FindByLinkText()
ff.test()