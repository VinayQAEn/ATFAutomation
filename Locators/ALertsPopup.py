from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
class Alertsandpopups:
    alt_simplealert_Xpath =  "//button[@id='alertBtn']"
    alt_confirmation_alert_xpath = "//button[@id='confirmBtn']"
    alt_promt_alert_Xpath = "//button[@id='promptBtn']"

    def __init__(self,driver):
        self.driver = driver
    def simple_alert(self):
        self.driver.find_element(By.XPATH, self.alt_simplealert_Xpath).click()
        self.myalert = self.driver.switch_to.alert
        self.myalert.accept()
    def confirmationalert(self):
        self.driver.find_element(By.XPATH,self.alt_confirmation_alert_xpath).click()
        self.myalert1 = self.driver.switch_to.alert
        self.myalert1.dismiss()
    def promtalert(self):
        self.driver.find_element(By.XPATH,self.alt_promt_alert_Xpath).click()
        self.myalert2 = self.driver.switch_to.alert
        self.myalert2.send_keys("Vinay")
        self.myalert2.accept()
        
        


