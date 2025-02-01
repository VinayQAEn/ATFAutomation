from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class Mousehover:
    btn_pointme_xpath = "//button[normalize-space()='Point Me']"
    lnk_mobile_xpath = "//*[@id='HTML3']/div[1]/div/div/a[1]"
    lnk_laptop_xpath = "//*[@id='HTML3']/div[1]/div/div/a[2]"
    def __init__(self,driver):
        self.driver = driver
    def get_mousehover(self):
        self.pointme = self.driver.find_element(By.XPATH,self.btn_pointme_xpath).click()
        self.mobile = self.driver.find_element(By.XPATH,self.lnk_mobile_xpath)
        self.laptop = self.driver.find_element(By.XPATH,self.lnk_laptop_xpath)
        self.act = ActionChains(self.driver)
        self.act.move_to_element(self.mobile).move_to_element(self.laptop).click().perform()
        

        