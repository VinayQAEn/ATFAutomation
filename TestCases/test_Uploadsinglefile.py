import pytest
from Locators.UploadSinglefile import Uploadsinglefile
from Utilities.customlogger import customlogger
@pytest.mark.usefixtures("setup")
class TestUploadSingleFile:
    def test_upload_single_file(self):
        self.logger = customlogger.get_logger(self)
        self.uploadsinglefile = Uploadsinglefile(self.driver)
        self.uploadsinglefile.get_uploadsinglefile()
        self.logger.info("File is uploaded")