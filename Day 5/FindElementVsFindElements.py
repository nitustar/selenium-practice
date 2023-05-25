import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("Selenium Drivers/chromedriver_win32/chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=serv_obj, options=options)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# 1. Find_Element - Return Single WebElement
# Locator matching with single webElement

# elem = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# elem.send_keys("Apple MacBook Pro 13-inch")

# Locator Matching with multiple webElement
# element = driver.find_element(By.XPATH, "//div[@class='footer']//a")
# print(element.text)         # Printing first Element : "Sitemap

# Element is not available then throw NoSuchElementException
# login_element = driver.find_element(By.LINK_TEXT, "Log")
# login_element.click()


# 2. Find_Elements - Return Multiple WebElement

# Locator matching with single webElement
# elem = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
# print(len(elem))
# elem[0].send_keys("Apple MacBook Pro 14-inch")

# Locator Matching with multiple webElement
# elements = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
# print(elements[0].text)         # Printing first Element : "Sitemap

# for elem in elements :
#     print(elem.text, end=",")


# Element is not available then throw NoSuchElementException
login_element = driver.find_elements(By.LINK_TEXT, "Log")
# login_element.click()
print(len(login_element))       # 0

time.sleep(3)
driver.close()