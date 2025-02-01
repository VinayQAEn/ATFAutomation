from selenium.webdriver.common.by import By
class Newtab:
    btn_newtab_xpath = "//button[normalize-space()='New Tab']"
    def __init__(self,driver):
        self.driver = driver
    def get_newtab(self):
        self.driver.find_element(By.XPATH, self.btn_newtab_xpath).click()
        self.WindowsIDS = self.driver.window_handles
        self.parentwindow = self.WindowsIDS[0]
        self.childwindow = self.WindowsIDS[1]
        self.driver.switch_to.window(self.parentwindow)
        self.driver.switch_to.window(self.childwindow)
        print(self.driver.title)
        self.driver.switch_to.window(self.parentwindow)
        print(self.driver.title)



