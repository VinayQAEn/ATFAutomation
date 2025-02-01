import pytest
from Locators.Datepicker3 import Datepicker3
from Utilities.customlogger import customlogger
@pytest.mark.usefixtures("setup")
class Test_Datepicker3:
    def test_datepicker3(self):
        self.datepicker = Datepicker3(self.driver)
        self.log = customlogger()
        self.logger = self.log.get_logger()
        self.logger.info("**********TestDatepicker3_001*********")
        self.datepicker.get_datepicker3()
        self.logger.info("Date is selected")
        self.logger.info("**********TestDatepicker3_001 Finished*********")