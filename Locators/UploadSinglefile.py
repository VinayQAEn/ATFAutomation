from selenium.webdriver.common.by import By
import time

class Uploadsinglefile:
    txt_uploadsinglefile_Xpath = "//input[@id='singleFileInput']"
    btn_uploadsinglefile_Xpath = "//button[@class='submit-btn']"
    def __init__(self, driver):
        self.driver = driver
    def get_uploadsinglefile(self):
        self.uploadsinglefile = self.driver.find_element(By.XPATH,self.txt_uploadsinglefile_Xpath)
        self.uploadsinglefile.send_keys("/Users/riyabakoria/Downloads/test.png")
        time.sleep(5)
        self.submit = self.driver.find_element(By.XPATH,self.btn_uploadsinglefile_Xpath)
        self.submit.click()
        time.sleep(5)
        print(self.uploadsinglefile.get_attribute("value")) 
        print("File is uploaded")