import pytest
from Locators.StaticWebTable import StaticWebTable
from Utilities.customlogger import customlogger
@pytest.mark.usefixtures("setup")
class TestStaticWebTable:
    @pytest.mark.regression
    def test_static_web_table(self):
        self.logger = customlogger.get_logger(self)
        self.staticwebtable = StaticWebTable(self.driver)
        self.staticwebtable.get_staticwebtable()
        self.logger.info("Static Web Table is displayed")
        self.logger.info("***********Test Static Web Table is passed***********")