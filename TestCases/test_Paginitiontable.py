
import pytest

from Locators.Paginitionwebtable import Paginitiontable
from Utilities.customlogger import customlogger
@pytest.mark.usefixtures('setup')
class Test_pagnitiontable:
    def test_pagnitiontable(self):
        self.pt = Paginitiontable(self.driver)
        self.log = customlogger()
        self.log = self.log.get_logger()
        self.log.info('*********Test Pagnition table*******')
        self.pt.get_pagnitiontable()
        self.log.info("*************Test pagnition table finished*******")
        
