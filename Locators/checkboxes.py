import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
class Checkboxes:
    checkboxes_Xpath = "//input[@class='form-check-input' and contains(@id,'day')]"
    def __init__(self, driver):
        self.driver = driver
    def click_checkboxes(self):
        self.checkboxes = self.driver.find_elements(By.XPATH,self.checkboxes_Xpath)

        
        
        
        for checkbox in self.checkboxes:
            checkbox.click()
        
        for i in range(len(self.checkboxes)):
            self.checkboxes[i].click()
        
        for i in range(len(self.checkboxes)-2,len(self.checkboxes)):
            self.checkboxes[i].click()
        
        for i in range(len(self.checkboxes)):
            if i>4:
                self.checkboxes[i].click()

    

            