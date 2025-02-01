import pytest
from Locators.animaldrp import AnimalDrp
from Utilities.customlogger import customlogger
@pytest.mark.usefixtures("setup")
class Test_AnimalDrp:
    def test_animalDrp(self):
        self.animal = AnimalDrp(self.driver)
        self.log = customlogger()
        self.logger = self.log.get_logger()
        self.logger.info("**********TestAnimalDrp_001*********")
        self.animal.get_animalclick()
        self.logger.info("Clicked on animal dropdown")
        self.animal.get_allanimals()
        self.logger.info("All animals are displayed")
        self.logger.info("**********TestAnimalDrp_001 Finished*********")
    
    