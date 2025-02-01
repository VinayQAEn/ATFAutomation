from selenium.webdriver.common.by import By

class UserregistrationPage:
    Txt_Name_Xpath = "//input[@id='name']"
    Txt_Email_Xpath = "//input[@id='email']"    
    Txt_Phone_Xpath = "//input[@id='phone']"
    Txt_Address_Xpath = "//textarea[@id='textarea']"
    Rd_Btn_Male_Xpath = "//input[@id='male']"
    Rd_Btn_Female_Xpath = "//input[@id='female']"

    def __init__(self, driver):
        self.driver = driver
    def enter_name(self, name):
        self.driver.find_element(By.XPATH, self.Txt_Name_Xpath).clear()
        self.driver.find_element(By.XPATH, self.Txt_Name_Xpath).send_keys(name)
    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.Txt_Email_Xpath).clear()
        self.driver.find_element(By.XPATH, self.Txt_Email_Xpath).send_keys(email)
    def enter_phone(self, phone):
        self.driver.find_element(By.XPATH, self.Txt_Phone_Xpath).clear()
        self.driver.find_element(By.XPATH, self.Txt_Phone_Xpath).send_keys(phone)
    def enter_address(self, address):       
        self.driver.find_element(By.XPATH, self.Txt_Address_Xpath).clear()
        self.driver.find_element(By.XPATH, self.Txt_Address_Xpath).send_keys(address)
    def click_rd_btnmale(self):
        self.male_radio = self.driver.find_element(By.XPATH,self.Rd_Btn_Male_Xpath)
        self.male_radio.click()
        print(self.male_radio.is_selected())
        print(self.male_radio.is_enabled())
        print(self.male_radio.is_displayed())
    def click_rd_btnfemale(self):
        self.female_radiobtn = self.driver.find_element(By.XPATH,self.Rd_Btn_Female_Xpath)
        self.female_radiobtn.click()
        print(self.female_radiobtn.is_selected())
        print(self.female_radiobtn.is_enabled())
        print(self.female_radiobtn.is_displayed())
