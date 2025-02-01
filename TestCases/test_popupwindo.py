import pytest
from Locators.Popupwindow import Popupwindow
from Utilities.customlogger import customlogger
@pytest.mark.usefixtures('setup')
class Test_popwindow:
    def test_popwindow(self):
        self.pw = Popupwindow(self.driver)
        self.logger = customlogger()
        self.log = self.logger.get_logger()
        self.log.info("*******Test popupwindow_001*******")
        self.pw.get_popwindow()



