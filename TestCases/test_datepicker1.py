import pytest
from Locators.Datepicker1 import Datepicker1
from Utilities.customlogger import customlogger
@pytest.mark.usefixtures("setup")
class Test_Datepicker1:
    def test_datepicker1(self):
        self.datepicker = Datepicker1(self.driver)
        self.log = customlogger()
        self.logger = self.log.get_logger()
        self.logger.info("**********TestDatepicker1_001*********")
        self.datepicker.get_datepicker()
        self.logger.info("Date is selected")
        self.logger.info("**********TestDatepicker1_001 Finished*********")