import pytest

from Utilities.customlogger import customlogger
from Locators.Dropdown import Dropdown


@pytest.mark.usefixtures("setup")
class Test_Country_Dropdown_001:
    def test_country_dropdown(self):
        self.log = customlogger()
        self.log = self.log.get_logger()
        self.log.info("**************Test_Country_Dropdown_001**************")
        self.cd = Dropdown(self.driver)
        self.cd.click_countrydrp()
        self.log.info("**************Test_Country_Dropdown_001_clicked sucessfully**************")
        self.cd.select_country("India")
        self.log.info("**************Test_Country_Dropdown_001_selected country successfully**************")
        self.cd.select_country("USA")
        self.log.info("**************Test_Country_Dropdown_001_selected country successfully**************")
        self.log.info("**************Test_Country_Dropdown_001 Finished**************") 