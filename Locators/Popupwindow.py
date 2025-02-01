import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Popupwindow:
    btn_newwindow_xpath = "//button[normalize-space()='New Tab']"
    def __init__(self,driver):
        self.driver = driver
    def get_popwindow(self):
        self.driver.find_element(By.XPATH, self.btn_newwindow_xpath).click()
        time.sleep(4)
        print(self.driver.title)

