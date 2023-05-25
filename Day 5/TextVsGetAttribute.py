import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("Selenium Drivers/chromedriver_win32/chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=serv_obj, options=options)
driver.get("https://admin-demo.nopcommerce.com/")

emailTextBox = driver.find_element(By.XPATH, "//input[@id='Email']")
emailTextBox.clear()
emailTextBox.send_keys("abc@gmail.com")

# text will take value of inner text of the element
# print("Result of text:", emailTextBox.text)
#
# # get_attribute will take any value of attribute inside the element.
# print("Result of get_attribute:", emailTextBox.get_attribute('value'))

button = driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")
print("Result of text:", button.text)
print("Result of get_attribute:", button.get_attribute('value'))
print("Result of get_attribute:", button.get_attribute('type'))

driver.close()