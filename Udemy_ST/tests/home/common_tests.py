from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class LoginTests():

    def test_validLogin(self):
        baseURL = "https://www.udemy.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        loginLink = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[3]/div[6]/a")
        loginLink.click()


        emailField = driver.find_element(By.ID, "email--1")
        emailField.send_keys("andreypetrov1@gmail.com")

        time.sleep(3)

        passwordField = driver.find_element(By.ID, "id_password")
        passwordField.send_keys("Gopikirotia#1")

        submitbutton = driver.find_element(By.ID, "submit-id-submit")
        submitbutton.click()

        time.sleep(3)
        searchBox = driver.find_element_by_name('q')
        searchBox.send_keys("The Web Developer Bootcamp 2021")

        searchButton = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[3]/div[2]/form/button")
        searchButton.click()
        time.sleep(3)
        course = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[1]/a/div")
        course.click()

        time.sleep(3)

        buyNow = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[5]/div/button")
        buyNow.click()

        time.sleep(3)

        selectState = driver.find_element(By.ID, "billingAddressSecondarySelect")
        selectState.click()
        delhi = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div[2]/form/div[1]/div/div[2]/div[2]/div[2]/div/div/select/option[11]")
        delhi.click()

        cardName = driver.find_element(By.ID, "fullname")
        cardName.send_keys("S A")

        mm = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div[2]/form/div[1]/div/div[3]/div/div[6]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/select")
        mm.click()
        nov = driver.find_element(By.XPATH,
                                    "/html/body/div[1]/div[2]/div/div/div/div[2]/form/div[1]/div/div[3]/div/div[6]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/select/option[12]")
        nov.click()

        yyyy = driver.find_element(By.XPATH,
                                 "/html/body/div[1]/div[2]/div/div/div/div[2]/form/div[1]/div/div[3]/div/div[6]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/select")
        yyyy.click()
        T23 = driver.find_element(By.XPATH,
                                  "/html/body/div[1]/div[2]/div/div/div/div[2]/form/div[1]/div/div[3]/div/div[6]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/select/option[4]")
        T23.click()

        cardNo = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div[2]/form/div[1]/div/div[3]/div/div[6]/div/div/div[1]/div/div[2]/div/div/input")
        cardNo.send_keys("8484448")

        cardcvv = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div[2]/form/div[1]/div/div[3]/div/div[6]/div/div/div[1]/div/div[3]/div[2]/div/input")
        cardcvv.send_keys("777")

        actions = ActionChains(driver)

        element = driver.find_element(By.CSS_SELECTOR, ".user-profile-dropdown--dropdown-button-avatar--Cbd6V")
        actions.move_to_element(element).perform()

        logoutlink = driver.find_element(By.XPATH,
                                              "/html/body/div[2]/div[1]/div[3]/div[9]/div/div/div/div/div/ul[6]/li[2]/a/div")
        logoutlink.click()

ff = LoginTests()
ff.test_validLogin()