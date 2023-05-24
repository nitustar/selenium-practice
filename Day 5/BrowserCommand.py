import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("Selenium Drivers/chromedriver_win32/chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=serv_obj, options=options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

time.sleep(2)
# driver.close()      # This command will close current tab from the browser.

driver.quit()       # This command will close all tab from the browser.


print("successfull.")
