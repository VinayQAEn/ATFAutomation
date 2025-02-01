from selenium.webdriver.common.by import By

class Dropdown:
    drp_country_xpath = "//select[@id='country']"
    drp_countries_xpath = "//select[@id='country']/option"
    def __init__(self, driver):
        self.driver = driver
    def click_countrydrp(self):
        self.driver.find_element(By.XPATH,self.drp_country_xpath).click()
        self.countryname = self.driver.find_element(By.XPATH,self.drp_country_xpath).get_attribute("value")
        print(self.countryname)

        
    def select_country(self, country):
        self.countries = self.driver.find_elements(By.XPATH,self.drp_countries_xpath)
        for c in self.countries:
            if c.text == country:
                c.click()
                break
        self.driver.find_element(By.XPATH,self.drp_country_xpath).get_attribute("value")
        print(self.driver.find_element(By.XPATH,self.drp_country_xpath).get_attribute("value"))
    
    
    