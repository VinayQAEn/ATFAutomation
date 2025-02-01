import pytest
from Locators.NewTab import Newtab
from Utilities.customlogger import customlogger
@pytest.mark.usefixtures('setup')
class Test_newtab:
    def test_newtab(self):
        self.nt = Newtab(self.driver)
        self.logger = customlogger()
        self.log = self.logger.get_logger()
        self.log.info("*****Test New tab_001********")
        self.nt.get_newtab()
        self.log.info("**********Test finished*******")
