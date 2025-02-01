import pytest
from Locators.Datepicker2 import Datepicker2
from Utilities.customlogger import customlogger
@pytest.mark.usefixtures("setup")
class Test_Datepicker2:
    def test_datepicker2(self):
        self.datepicker = Datepicker2(self.driver)
        self.log = customlogger()
        self.logger = self.log.get_logger()
        self.logger.info("**********TestDatepicker2_001*********")
        self.datepicker.get_datepicker2()
        self.logger.info("Date is selected")
        self.logger.info("**********TestDatepicker2_001 Finished*********")