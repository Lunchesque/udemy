from selenium import webdriver
from MethodsAndProperties.handy_wrappers import HandyWrappers
from selenium.webdriver.common.action_chains import ActionChains

class ExplicitWaitDemo():

    def test(self):
        baseUrl = "https://www.expedia.com"
        driver = webdriver.Chrome()
        wrapper = HandyWrappers(driver)
        driver.implicitly_wait(0.5)
        driver.maximize_window()
        driver.get(baseUrl)

        wrapper.getElement("//button[@id='tab-flight-tab-hp']").click()
        wrapper.getElement("//input[@id='flight-origin-hp-flight']").send_keys("SFO")
        wrapper.getElement("//input[@id='flight-destination-hp-flight']").send_keys("NYC")
        wrapper.getElement("//input[@id='flight-departing-hp-flight']").send_keys("03/01/2018")
        returnDate = wrapper.getElement("//input[@id='flight-returning-hp-flight']")
        returnDate.clear()
        returnDate.send_keys("03/03/2018")
        searchBtn = wrapper.getElement("//form[@id='gcw-flights-form-hp-flight']//div[@class='cols-nested']//label[@class='col search-btn-col']//button[@type='submit']")
        ActionChains(driver).move_to_element(searchBtn).click(searchBtn).perform()
        wrapper.getElement("//input[@id='stopFilter_stops-0']").click()

        ActionChains(driver).pause(3).perform()


ff = ExplicitWaitDemo()
ff.test()




