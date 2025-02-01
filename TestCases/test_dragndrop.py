import pytest
import time
from Utilities.customlogger import customlogger
from Locators.DragNDrop import DragNDrop

@pytest.mark.usefixtures('setup')
class Test_dragndrop:
    @pytest.mark.regression
    def test_dragndrop(self):
        self.logger = customlogger()
        self.dd = DragNDrop(self.driver)
        self.log = self.logger.get_logger()
        self.log.info("*****Test_drag and drop_001******")
        self.dd.get_dragndrop()
        time.sleep(10)
        
