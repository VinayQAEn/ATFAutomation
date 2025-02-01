from selenium.webdriver.common.by import By

class Colordrp:
    drp_color_Xpath = "//select[@id='colors']"
    drp_allcolors_Xpath = "//select[@id='colors']/option"
    def __init__(self,driver):
        self.driver = driver
    def get_colorclick(self):
        self.driver.find_element(By.XPATH, self.drp_color_Xpath).click()
    def get_allcolors(self):
        self.all_colors = self.driver.find_elements(By.XPATH, self.drp_allcolors_Xpath)
        for color in self.all_colors:
            print(color.text)
            if color.text == "Red":
                color.click()
                break
        
    