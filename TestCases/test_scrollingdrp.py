import pytest
import time
from Locators.scrollingdrp import ScrollingDrp
from Utilities.customlogger import customlogger
@pytest.mark.usefixtures('setup')
class Test_scrollingdrp:
    def test_scrollingdrp(self):
        self.logger = customlogger()
        self.sd = ScrollingDrp(self.driver)
        self.log = self.logger.get_logger()
        self.log.info("********Testscrollingdrp_001*******")
        self.sd.get_scrollingdrp()
        time.sleep(5)
        