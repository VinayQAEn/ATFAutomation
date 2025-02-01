import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
class Doubleclick:
    btn_copytext_xpath = "//button[normalize-space()='Copy Text']"
    def __init__(self,driver):
        self.driver = driver
    def get_doubleclick(self):
        self.act = ActionChains(self.driver)
        self.btn = self.driver.find_element(By.XPATH,self.btn_copytext_xpath)
        self.act.double_click(self.btn).perform()
        time.sleep(5)


        