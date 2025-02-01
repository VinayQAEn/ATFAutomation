from selenium import webdriver
from selenium.webdriver.common.by import By
class Dyanamicwebtable:
    noofrows_Xpath = "//table[@id='taskTable']/tbody/tr"
    noocolumn_Xpath = "//table[@id='taskTable']/thead/tr/th"
    def __init__(self,driver):
        self.driver = driver

    def get_dynamictable(self):
        self.Row = len(self.driver.find_elements(By.XPATH, self.noofrows_Xpath))
        self.Column = len(self.driver.find_elements(By.XPATH,self.noocolumn_Xpath))
        for r in range(1,self.Row+1):
            for c in range(1,self.Column+1):
                self.Data = self.driver.find_element(By.XPATH,"//table[@id='taskTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
                print(self.Data,end="  ")
            print()






