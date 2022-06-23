from selenium import webdriver
import os

driverLocation = "C:\\Users\\Sanskar\\workspace\\lib\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = driverLocation
driver = webdriver.Chrome(driverLocation)

driver.get("http://www.google.com")
myPageTitle = driver.title
print(myPageTitle)

