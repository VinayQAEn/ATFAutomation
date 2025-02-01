from re import S
from selenium.webdriver.common.by import By

class ScrollingDrp:
    drp_scrolling_Xpath = "//div[@id='dropdown']/div"
    txt_drp_xpath = "//input[@id='comboBox']"
    def __init__(self,driver):
        self.driver = driver
    def get_scrollingdrp(self):
        self.driver.find_element(By.XPATH,self.txt_drp_xpath).click()
        self.all_items = self.driver.find_elements(By.XPATH,self.drp_scrolling_Xpath)
        for item in self.all_items:
            print(item.text)
            if item.text == "Item 100":
                item.click()
