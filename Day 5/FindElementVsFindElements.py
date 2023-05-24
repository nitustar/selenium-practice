import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("Selenium Drivers/chromedriver_win32/chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=serv_obj, options=options)
driver.get("https://demo.nopcommerce.com/")


# Find_Element - Return Single WebElement
# Locator matching with single webElement

# elem = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# elem.send_keys("Apple MacBook 13 inch")

# Locator Matching with multiple webElement
driver.find_element(By.XPATH, "//div[@class='footer']//a")

time.sleep(3)
driver.close()