from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCSVData("testdata.csv"))
    @unpack
    def test_t2validLogin(self, cardName, cardNo, cardCvv):
        self.log.info("*#" * 20)
        self.log.info("test_t2validLogin started")
        self.log.info("*#" * 20)
        #self.lp.logout()
        #self.lp.login("andreypetrov1@gmail.com", "Gopikirotia#1")
        result1 = self.lp.verifyLoginTitle()
        time.sleep(5)
        self.ts.mark(result1, "Title Verification")
        self.lp.navigateCourse()
        self.lp.enterDetails(uname=cardName, unum=cardNo, ucvv=cardCvv)
        self.lp.mainPage()

    """
    @pytest.mark.run(order=2)
    def test_t1invalidLogin(self):
        self.log.info("*#" * 20)
        self.log.info("test_t1invalidLogin started")
        self.log.info("*#" * 20)
        self.lp.logout()
        self.lp.login("andreypetrov1@gmail.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True
    """