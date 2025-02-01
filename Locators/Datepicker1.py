from selenium.webdriver.common.by import By

class Datepicker1:
    txt_datepicker = "//input[@id='datepicker']"
    Month = "January"
    Year = "1996"
    Date = "30"
    def __init__(self, driver):
        self.driver = driver
    def get_datepicker(self):
        self.driver.find_element(By.XPATH, self.txt_datepicker).click()
        while True:
            self.month = self.driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']")
            self.year = self.driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']")
            if self.month.text == self.Month and self.year.text == self.Year:
                break
            else:
                self.driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()
        
        Dates = self.driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
        for date in Dates:
            if date.text == self.Date:
                date.click()
                break
        print(self.driver.find_element(By.XPATH, self.txt_datepicker).get_attribute("value"))
        
        
        