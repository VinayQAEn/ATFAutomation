import pytest

from Locators.Dynamic_webTable import Dyanamicwebtable
from Utilities.customlogger import customlogger

@pytest.mark.usefixtures("setup")
class TestDyanamictable:
    def test_dynamictable(self):
        self.dt = Dyanamicwebtable(self.driver)
        self.logger = customlogger()
        self.log = self.logger.get_logger()
        self.log.info('**********Testdynamictable_001********')
        self.dt.get_dynamictable()
        self.log.info("Testdynamic table finished")

        
