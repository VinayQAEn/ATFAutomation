import pytest

from Utilities.customlogger import customlogger
from Locators.checkboxes import Checkboxes

@pytest.mark.usefixtures("setup")
class Test_Checkboxes_001:
    def test_checkboxes(self):
        self.log = customlogger()
        self.log = self.log.get_logger()
        self.log.info("**************Test_Checkboxes_001**************")
        self.cb = Checkboxes(self.driver)
        self.cb.click_checkboxes()
        self.log.info("**************Test_Checkboxes_001 Finished**************")
   