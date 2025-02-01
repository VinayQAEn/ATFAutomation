from selenium.webdriver.common.by import By

class AnimalDrp:
    drp_animal_Xpath = "//select[@id='animals']"
    drp_allanimals_Xpath = "//select[@id='animals']/option"

    def __init__(self, driver):
        self.driver = driver    
    def get_animalclick(self):
        self.driver.find_element(By.XPATH, self.drp_animal_Xpath).click()
    def get_allanimals(self):
        self.all_animals = self.driver.find_elements(By.XPATH, self.drp_allanimals_Xpath)
        for animal in self.all_animals:
            print(animal.text)
            if animal.text == "Elephant":
                animal.click()
                break
        