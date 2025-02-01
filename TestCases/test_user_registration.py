import pytest
from Locators.userregistration import UserregistrationPage
from Utilities.customlogger import customlogger
from Utilities.Readconfig import ReadConfig  # Add this line to import the ReadConfig class
@pytest.mark.usefixtures("setup")
class Test_User_Registration_001:
    name = ReadConfig.get_name()
    email = ReadConfig.get_email()
    phone = ReadConfig.get_phone()
    address = ReadConfig.get_address()
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_user_registration(self):
        self.ur = UserregistrationPage(self.driver)
        self.log = customlogger()
        self.log = self.log.get_logger()
        self.log.info("**************Test_User_Registration_001**************")
        self.ur.enter_name(self.name)
        self.ur.enter_email(self.email)
        self.ur.enter_phone(self.phone)
        self.ur.enter_address(self.address)
        self.ur.click_rd_btnmale()
        self.ur.click_rd_btnfemale()
        

        