from pages.home.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = NavigationPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_t1(self):
        self.lp.navigate1()
        result1 = self.lp.verifyManageAccTitle()
        self.ts.mark(result1, "Manage Account Title Verification")

        self.lp.navigate2()
        result1 = self.lp.verifyCreativeCloudTitle()
        self.ts.mark(result1, "Creative Cloud Title Verification")

        self.lp.navigate3()
        result1 = self.lp.verifyPhotoshopTitle()
        self.ts.mark(result1, "Photoshop Title Verification")

        self.lp.navigate4()
        result1 = self.lp.verifyAcrobatTitle()
        self.ts.mark(result1, "Acrobat Title Verification")
