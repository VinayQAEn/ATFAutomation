from re import S
import pytest
from Utilities.customlogger import customlogger
from Locators.Double_click import Doubleclick
@pytest.mark.usefixtures('setup')
class Test_Doubleclick:
    def test_doubleclick(self):
        self.logger = customlogger()
        self.log = self.logger.get_logger()
        self.log.info('*********Test Doubleclick_001**********')
        self.dc = Doubleclick(self.driver)
        self.dc.get_doubleclick()
        self.log.info("**********Test finished_doubleclick*******")
        