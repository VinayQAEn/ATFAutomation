from re import S
import pytest
from Locators.Mousehover import Mousehover
from Utilities.customlogger import customlogger
@pytest.mark.usefixtures('setup')
class Test_mousehover:
    def test_mousehover(self):
        self.Mh = Mousehover(self.driver)
        self.logger = customlogger()
        self.log = self.logger.get_logger()
        self.log.info("*******Test Mousehover_001********")
        self.Mh.get_mousehover()
        

