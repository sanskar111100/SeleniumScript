""""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LoginTests():

    def test_validLogin(self):
        baseURL = "https://www.adobe.com/in/creativecloud.html?gclid=CjwKCAjw07qDBhBxEiwA6pPbHtFf_Z1eoQLhfbczXBeyTkrEt5nFyv9hKQy7pb4EyRiRHiJ7_FACfxoCfKIQAvD_BwE&sdid=SL4KMHQ2&mv=search&ef_id=CjwKCAjw07qDBhBxEiwA6pPbHtFf_Z1eoQLhfbczXBeyTkrEt5nFyv9hKQy7pb4EyRiRHiJ7_FACfxoCfKIQAvD_BwE:G:s&s_kwcid=AL!3085!3!473191825332!e!!g!!adobe!221174348!17525765828"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        loginLink = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/header/nav/div/ul/li/div/ul/li/div/ul/li[3]/div/ul/li[2]/div/a")
        loginLink.click()

        emailField = driver.find_element(By.ID, "EmailPage-EmailField")
        emailField.send_keys("sanskar111100@gmail.com")

        continuebutton = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/section/div/div/section/div/section/div/div/section/section/form/section[2]/div[2]/button")
        continuebutton.click()

        time.sleep(10)

        passwordField = driver.find_element(By.ID, "PasswordPage-PasswordField")
        passwordField.send_keys("Gopikirotia#1")

        submitbutton = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/section/div/div/section/div/section/div/div/section/section/form/section[2]/div[2]/button")
        submitbutton.click()

        time.sleep(10)

        logoutButton = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div/header/nav/div/ul/li/div/ul/li/div/ul/li[3]/div/ul/li[2]/div/div/div/ul/li/a/div")
        logoutButton.click()
ff = LoginTests()
ff.test_validLogin()

"""

from pages.home.login_page import LoginPage
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
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_t2validLogin(self):
        self.log.info("*#" * 20)
        self.log.info("test_t2validLogin started")
        self.log.info("*#" * 20)
        self.lp.login("sanskar111100@gmail.com", "Password#1")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title Verification")
        result2 = self.lp.verifyLoginSuccessful()
        print("Result1: " + str(result1))
        print("Result2: " + str(result2))
        self.ts.markFinal("test_t2validLogin", result2, "Login Verification")

    @pytest.mark.run(order=2)
    def test_t1invalidLogin(self):
        self.log.info("*#" * 20)
        self.log.info("test_t1invalidLogin started")
        self.log.info("*#" * 20)
        self.lp.logout()
        self.lp.login("sanskar111100@gmail.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True






