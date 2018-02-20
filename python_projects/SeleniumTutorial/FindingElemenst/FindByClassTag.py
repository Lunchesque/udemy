from selenium import webdriver

class FindByLinkText():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        elementByClassName = driver.find_element_by_class_name("displayed-class")
        elementByClassName.send_keys("Test")

        if elementByClassName is not None:
            print("We found an element by Class Name")

        elementByTagName = driver.find_element_by_tag_name("h1")
        text = elementByTagName.text

        if elementByTagName is not  None:
            print("We found an element by Tag Name and the text of the element is: " + text)

ff = FindByLinkText()
ff.test()