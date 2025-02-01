from selenium.webdriver.common.by import By

class Datepicker3:
    txt_startdate_Xpath = "//input[@id='start-date']"
    txt_enddate_Xpathenddate = "//input[@id='end-date']"
    btn_submit_Xpath = "//button[@class='submit-btn']"

    def __init__(self, driver):
        self.driver = driver
    def get_datepicker3(self):
        self.startdate = self.driver.find_element(By.XPATH,self.txt_startdate_Xpath)
        self.startdate.send_keys("01/01/2020")
        self.enddate = self.driver.find_element(By.XPATH,self.txt_enddate_Xpathenddate)
        self.enddate.send_keys("01/01/2021")        
        self.submit = self.driver.find_element(By.XPATH,self.btn_submit_Xpath)
        self.submit.click()
        print(self.startdate.get_attribute("value")) 
        print(self.enddate.get_attribute("value"))