import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
class DragNDrop:
    source_element_Xpath = "//div[@id='draggable']"
    target_element_Xpath = "//div[@id='droppable']"
    def __init__(self,driver):
        self.driver = driver
    def get_dragndrop(self):
        self.act = ActionChains(self.driver)
        self.source_element = self.driver.find_element(By.XPATH, self.source_element_Xpath)
        self.target_element = self.driver.find_element(By.XPATH,self.target_element_Xpath)
        self.act.drag_and_drop(self.source_element,self.target_element).perform()
        time.sleep(5)



        