import traceback
from selenium import webdriver
import os

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseURL = "https://www.adobe.com/in/creativecloud.html?gclid=Cj0KCQjwmcWDBhCOARIsALgJ2Qch68d4p4b2dph7CRzVQzbT3RXyTgPjrmPpLYRtB_AaF1VvVNf6VPkaAscPEALw_wcB&sdid=SL4KMHQ2&mv=search&ef_id=Cj0KCQjwmcWDBhCOARIsALgJ2Qch68d4p4b2dph7CRzVQzbT3RXyTgPjrmPpLYRtB_AaF1VvVNf6VPkaAscPEALw_wcB:G:s&s_kwcid=AL!3085!3!446722869342!e!!g!!adobe!221174348!17525765828"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            chromedriver = "C:/Users/Sanskar/PycharmProjects/chromedriver"
            os.environ["webdriver.chrome.driver"] = chromedriver
            driver = webdriver.Chrome(chromedriver)
            driver.set_window_size(1440, 900)
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver