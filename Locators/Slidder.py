from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Slidder:
    firstelemnt_xpath = "//div[@id='HTML7']//span[1]"
    secondelement_xpath = "//div[@id='HTML7']//span[2]"
    def __init__(self,driver):
        self.driver = driver
    def get_slidder(self):
        self.act = ActionChains(self.driver)
        first_element = self.driver.find_element(By.XPATH, self.firstelemnt_xpath)
        second_element = self.driver.find_element(By.XPATH,self.secondelement_xpath)
        self.act.drag_and_drop_by_offset(first_element,100,0).perform()
        self.act.drag_and_drop_by_offset(second_element,-40,0).perform()
