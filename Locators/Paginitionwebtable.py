from selenium.webdriver.common.by import By

class Paginitiontable:
    tbl_checkboxes_Xpath = "//table[@id='productTable']/tbody/tr/td[4]/input"
    lnk_2_Xpath = "//a[normalize-space()='2']"
    def __init__(self,driver):
        self.driver = driver
    def get_pagnitiontable(self):
        self.checkboxes = self.driver.find_elements(By.XPATH, self.tbl_checkboxes_Xpath)
        for check in self.checkboxes:
            check.click()
        self.driver.find_element(By.XPATH,self.lnk_2_Xpath).click()
        
        