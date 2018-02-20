from selenium import webdriver

class FindByIdName():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        elementByName = driver.find_element_by_name("show-hide")
        elementById = driver.find_element_by_id("name")

        if elementByName is not None:
            print("We found element by name")

        if elementById is not None:
            print("We found a element by id")

        driver.find_element_by_id("dsfjhdshklsdkl")

ff = FindByIdName()
ff.test()