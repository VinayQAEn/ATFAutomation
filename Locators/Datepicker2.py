from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Datepicker2:
    txt_datepicker2 = "//input[@id='txtDate']"
    month_drp = "//select[@aria-label='Select month']"
    year_drp = "//select[@aria-label='Select year']"
    def __init__(self, driver):
        self.driver = driver
    def get_datepicker2(self):
        self.driver.find_element(By.XPATH, self.txt_datepicker2).click()
        self.Month = Select(self.driver.find_element(By.XPATH, self.month_drp))
        self.Month.select_by_visible_text("Jan")
        self.Year = Select(self.driver.find_element(By.XPATH, self.year_drp))
        self.Year.select_by_visible_text("2018")
        Dates = self.driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
        for date in Dates:
            if date.text == "30":
                date.click()
                break
        print(self.driver.find_element(By.XPATH, self.txt_datepicker2).get_attribute("value"))        