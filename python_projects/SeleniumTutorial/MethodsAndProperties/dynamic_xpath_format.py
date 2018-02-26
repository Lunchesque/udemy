from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from utilities.handy_wrappers import HandyWrappers


class DynamicXPathFormat():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        wrapper = HandyWrappers(driver)
        driver.implicitly_wait(5)
        driver.get(baseUrl)

        wrapper.getElement("//a[@href='/sign_in']").click()
        email = wrapper.getElement("//input[@id='user_email']")
        email.send_keys("test@email.com")
        password = wrapper.getElement("//input[@id='user_password']")
        password.send_keys("abcabc")
        wrapper.getElement("//input[@type='submit']").click()

        searchBox = wrapper.getElement("//input[@id='search-courses']")
        searchBox.send_keys("JavaScript")
        searchBtn = wrapper.getElement("//button[@id='search-course-button']")
        searchBtn.click()

        _course = "//div[contains(@class, 'course-listing-title') and contains(text(), '{0}')]"
        _courseLocator = _course.format("JavaScript for beginners")

        ActionChains(driver).pause(1).perform()

        courseElement = wrapper.getElement(_courseLocator)
        courseElement.click()

        ActionChains(driver).pause(3).perform()

ff = DynamicXPathFormat()
ff.test()