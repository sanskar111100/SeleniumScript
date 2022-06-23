import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging
import time
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/header/nav/div/ul/li/div/ul/li/div/ul/li[3]/div/ul/li[2]/div/a"
    _email_field = "EmailPage-EmailField"
    _continue_button = "/html/body/div[1]/div/div/section/div/div/section/div/section/div/div/section/section/form/section[2]/div[2]/button"
    _password_field = "PasswordPage-PasswordField"
    _login_button = "/html/body/div[1]/div/div/section/div/div/section/div/section/div/div/section/section/form/section[2]/div[2]/button"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def clickContinueButton(self):
        self.elementClick(self._continue_button, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        time.sleep(5)
        self.clickLoginLink()
        time.sleep(5)
        #self.clearFields()
        self.enterEmail(email)
        time.sleep(5)
        self.clickContinueButton()
        time.sleep(5)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        self.waitForElement("/html/body/div[1]/div/div[1]/div[2]/div/div/header/nav/div/ul/li/div/ul/li/div/ul/li[3]/div/ul/li[2]/div/div/a", locatorType="xpath")
        result = self.isElementPresent(locator="/html/body/div[1]/div/div[1]/div[2]/div/div/header/nav/div/ul/li/div/ul/li/div/ul/li[3]/div/ul/li[2]/div/div/a", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(locator="PasswordPage-PasswordField", locatorType="id")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Adobe: Creative, marketing and document management solutions")

    def logout(self):
        self.nav.navigateToUserSettings()
        logoutLinkElement = self.waitForElement(locator="/html/body/div[1]/div/div[1]/div[2]/div/div/header/nav/div/ul/li/div/ul/li/div/ul/li[3]/div/ul/li[2]/div/div/div/ul/li/a/div",
                          locatorType="xpath", pollFrequency=1)
        #self.elementClick(element=logoutLinkElement)
        self.elementClick(locator="/html/body/div[1]/div/div[1]/div[2]/div/div/header/nav/div/ul/li/div/ul/li/div/ul/li[3]/div/ul/li[2]/div/div/div/ul/li/a/div",
                          locatorType="xpath")

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()
