from selenium import webdriver
from utilities.handy_wrappers import HandyWrappers
from selenium.webdriver.common.action_chains import ActionChains

class SwitchToAlert():

     def switchToAlert(self):
         baseUrl = "https://letskodeit.teachable.com/p/practice"
         driver = webdriver.Chrome()
         wrap = HandyWrappers(driver)
         driver.maximize_window()
         driver.implicitly_wait(5)
         driver.get(baseUrl)

         inputElement = wrap.getElement("//input[@id='name']")
         inputElement.send_keys("Sergey")
         print("Inputed text")

         alertBtn = wrap.getElement("//input[@id='alertbtn']")
         alertBtn.click()
         print("Clicked ALERT button")
         ActionChains(driver).pause(2).perform()

         alert1 = driver.switch_to.alert
         alert1.accept()
         print("Clicked OK(accepted)")
         ActionChains(driver).pause(2).perform()

         confirmBtn = wrap.getElement("//input[@id='confirmbtn']")
         confirmBtn.click()
         print("Clicked CONFIRM button")
         ActionChains(driver).pause(2).perform()

         alert2 = driver.switch_to.alert
         alert2.accept()
         print("Accepted alert")
         ActionChains(driver).pause(2).perform()

         confirmBtn.click()
         print("Clicked CONFIRM button again")
         ActionChains(driver).pause(2).perform()

         alert3 = driver.switch_to.alert
         alert3.dismiss()
         print("Dismissed alert")
         ActionChains(driver).pause(2).perform()

ff = SwitchToAlert()
ff.switchToAlert()