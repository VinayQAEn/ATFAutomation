import pytest
import time
from selenium import webdriver
from Locators.Slidder import Slidder
from Utilities.customlogger import customlogger
@pytest.mark.usefixtures('setup')
class Test_slidder:
    @pytest.mark.regression
    def test_slidder(self):
        self.logger = customlogger()
        self.sl = Slidder(self.driver)
        self.log = self.logger.get_logger()
        self.log.info("********Test slidder_001********")
        self.sl.get_slidder()
        time.sleep(7)
