from selenium.webdriver.common.by import By

class StaticWebTable:
    Noofrows = "//table[@name='BookTable']/tbody/tr"
    Noofcolumns = "//table[@name='BookTable']/tbody/tr/th"
    def __init__(self, driver):
        self.driver = driver    
    def get_staticwebtable(self):
        rows = len(self.driver.find_elements(By.XPATH,self.Noofrows))
        columns = len(self.driver.find_elements(By.XPATH,self.Noofcolumns))
        print(rows)
        print(columns)
        for r in range(2,rows+1):
            for c in range(1,columns+1):
                value = self.driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
                print(value,end="  ")
            print()
        
        for r in range(2,rows+1):
            for c in range(1,columns+1):
                value = self.driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
                if value == "Learn JavaScript":
                    self.driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]/following-sibling::td[1]/input").click()
                    break
        
        for r in range(2,rows+1):
            for c in range(1,columns+1):
                value = self.driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
                if value == "Learn Python":
                    self.driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]/following-sibling::td[1]/input").click()
                    break
        
        for r in range(2,rows+1):
                value = self.driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
                if value == "Mukesh":
                    self.bookname = self.driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
                    self.price = self.driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text
                    print(self.bookname,self.price,end="  ")
                print()
        
        