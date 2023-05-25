import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("Selenium Drivers/chromedriver_win32/chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=serv_obj, options=options)
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")

driver.maximize_window()

# is_displayed() and is_enabled  (WEB ELEMENT) -> used for validation purpose

search_box = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")

print("Display Status:", search_box.is_displayed())     # True
print("Enable Status:", search_box.is_enabled())        # True

# is_selected()  is for radioButton and checkBox

rd_male = driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH,"//input[@id='gender-female']")

print("Default radio button status.")
print("Male Status: ", rd_male.is_selected())        # False
print("Female Status: ", rd_female.is_selected())      # False

time.sleep(2)

rd_male.click()

print("After selecting a radio button.")
print("Male Status: ", rd_male.is_selected())        # True
print("Female Status: ", rd_female.is_selected())      # False

time.sleep(2)

rd_female.click()

print("After selecting a radio button.")
print("Male Status: ", rd_male.is_selected())        # False
print("Female Status: ", rd_female.is_selected())      # True

time.sleep(2)

driver.quit()