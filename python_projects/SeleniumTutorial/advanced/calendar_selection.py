from selenium import webdriver
from utilities.handy_wrappers import HandyWrappers
from utilities.explicit_wait_type import ExplicitWaitType
from selenium.webdriver.common.action_chains import ActionChains

class CalendarSelection():

    def test1(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        wrapper = HandyWrappers(driver)
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        #Click flights tab
        wrapper.getElement("//button[@id='tab-flight-tab-hp']").click()
        #Find departing field
        depField = wrapper.getElement("//input[@id='flight-departing-hp-flight']")
        #Click departing field
        depField.click()
        #Find the date to select
        dateToSelect = wrapper.getElement("//div[@class='col gcw-date-field']//div[2]//button[text()='26']")
        #Click the date
        dateToSelect.click()

        ActionChains(driver).pause(3).perform()

ff = CalendarSelection()
ff.test1()