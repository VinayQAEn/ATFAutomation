import pytest
from Locators.ALertsPopup import Alertsandpopups
from Utilities.customlogger import customlogger
@pytest.mark.usefixtures('setup')
class Test_alertandpopups:
    def test_alaertsandpopups(self):
        self.at = Alertsandpopups(self.driver)
        self.logger = customlogger()
        self.log = self.logger.get_logger()
        self.log.info("**********Test alertand popups statted*********")
        self.at.simple_alert()
        self.at.confirmationalert()
        self.at.promtalert()
        self.log.info("*********test finished*************")

