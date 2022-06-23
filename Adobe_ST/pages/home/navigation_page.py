import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _user_settings_icon = "/html/body/div[1]/div/div[1]/div[2]/div/div/header/nav/div/ul/li/div/ul/li/div/ul/li[3]/div/ul/li[2]/div/div/a"


    def navigateToUserSettings(self):
        userSettingsElement = self.waitForElement(locator=self._user_settings_icon, locatorType="xpath", pollFrequency=1)
        #self.elementClick(element=userSettingsElement)
        self.elementClick(locator=self._user_settings_icon, locatorType="xpath")

    def navigate1(self):
        self.elementClick("//div[@id='id-0ef06093f7ff28f2eb59d8bc6cfebc72']/div/div/div/a/span", locatorType="xpath")
        time.sleep(7)

    def navigate2(self):
        self.goback()
        self.elementClick("/html/body/div[1]/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/a", locatorType="xpath")
        time.sleep(5)

    def navigate3(self):
        self.goback()
        self.elementClick("(//div[@id='id-5b96f944b79b4586900cce2da372687a']/div/a)[2]", locatorType="xpath")
        time.sleep(3)

    def navigate4(self):
        self.goback()
        self.elementClick("(//div[@id='id-bd68e8542ddb63c543182e675b491375']/div/a)[2]", locatorType="xpath")
        time.sleep(3)

    def verifyManageAccTitle(self):
        return self.verifyPageTitle("Adobe Account")

    def verifyCreativeCloudTitle(self):
        return self.verifyPageTitle("Home | Adobe Creative Cloud")

    def verifyPhotoshopTitle(self):
        return self.verifyPageTitle("Photo, image & design editing software | Buy Adobe Photoshop")

    def verifyAcrobatTitle(self):
        return self.verifyPageTitle("Adobe: Creative, marketing and document management solutions")