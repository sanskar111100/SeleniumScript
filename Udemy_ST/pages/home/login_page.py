import utilities.custom_logger as cl
#from pages.home.navigation_page import NavigationPage
import logging
import time
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        #self.nav = NavigationPage(driver)

    # Locators
    _login_link = "/html/body/div[1]/div[1]/div[3]/div[6]/a" #"/html/body/div[1]/div[1]/div[3]/div[6]/a"
    _different_account = "/html/body/div[1]/div[2]/div[1]/div[3]/form/div[2]/div/div/a"
    _email_field = "email--1"
    _password_field = "id_password"
    _login_button = "submit-id-submit"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def clickDifferentAccount(self):
        self.elementClick(self._different_account, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="id")

    def login(self, email="", password=""):
        self.loginDone()
        """
        time.sleep(5)
        self.clickLoginLink()
        time.sleep(5)
        #self.clickDifferentAccount()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        """

    def navigateCourse(self):
        self.navigate()

    def enterDetails(self, uname, unum, ucvv):
        self.enterCardDetails(name=uname, num=unum, cvv=ucvv)

    def verifyLoginSuccessful(self):
        self.waitForElement("u681-popper-trigger--19", locatorType="id")
        result = self.isElementPresent(locator="u681-popper-trigger--19", locatorType="id")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(locator="/html/body/div[1]/div[2]/div[1]/div[3]/form/div[1]/div/div", locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Online Courses - Anytime, Anywhere | Udemy")

    def logout(self):
        self.logoutDone()

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

    def mainPage(self):
        self.gotoMainPage()
