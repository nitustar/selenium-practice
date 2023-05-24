import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("Selenium Drivers/chromedriver_win32/chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=serv_obj, options=options)
driver.get("https://www.snapdeal.com")
driver.maximize_window()
driver.get("https://www.amazon.in")

time.sleep(2)
driver.back()           # To go previous page on the Browser.
time.sleep(2)
driver.forward()        # To go last page on the Browser.
time.sleep(2)

driver.refresh()        # To reload the page on the Browser.

driver.close()