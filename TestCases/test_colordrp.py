import pytest
from Locators.Color_drp import Colordrp
from Utilities.customlogger import customlogger
@pytest.mark.usefixtures("setup")
class TestColorDrp:
    def test_colorDrp(self):
        color = Colordrp(self.driver)
        self.log = customlogger()
        self.logger = self.log.get_logger()
        self.logger.info("**********TestColorDrp_001*********")
        color.get_colorclick()
        self.logger.info("Clicked on color dropdown")
        color.get_allcolors()
        self.logger.info("All colors are displayed")
        self.logger.info("**********TestColorDrp_001 Finished*********")
        