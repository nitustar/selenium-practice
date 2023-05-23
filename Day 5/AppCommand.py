import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("Selenium Drivers/chromedriver_win32/chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=serv_obj, options=options)
driver.get("https://www.google.com/")           

# print title of the page
print(driver.title)             # Google

# print url of the page
print(driver.current_url)       # https://www.google.com/

print(driver.page_source)       # return source code of the application

time.sleep(2)
driver.quit()