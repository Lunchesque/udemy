from selenium import webdriver
from MethodsAndProperties.handy_wrappers import HandyWrappers
from selenium.webdriver.common.action_chains import ActionChains

class ImplicitWaitDemo():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        wrapper = HandyWrappers(driver)
        driver.get(baseUrl)

        loginLink = wrapper.getElement("//a[@href='/sign_in']")
        loginLink.click()

        emailField = wrapper.getElement("//input[@id='user_email']")
        emailField.send_keys("test@email.com")

ff = ImplicitWaitDemo()
ff.test()