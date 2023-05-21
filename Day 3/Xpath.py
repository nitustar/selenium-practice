import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("Selenium Drivers/chromedriver_win32/chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=serv_obj, options=options)
driver.get("http://automationpractice.pl/index.php")
driver.maximize_window()

# Absolute XPATH

# driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("T-shirt")
# driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button").click()

# Relative XPATH

# driver.find_element(By.XPATH, "//*[@id='search_query_top']").send_keys("T-shirt")
# driver.find_element(By.XPATH, "//*[@id='searchbox']/button").click()

# OR & AND

# driver.find_element(By.XPATH, "//input[@id='search_query_top' or @name='search_query']").send_keys("T-shirt")
# driver.find_element(By.XPATH, "//button[@name='submit_search' and @class='btn btn-default button-search']").click()

# contain() & starts-with()

driver.find_element(By.XPATH, "//input[contains(@id,'search')]").send_keys("T-shirt")
driver.find_element(By.XPATH, "//button[starts-with(@name,'submit')]").click()

# text()

driver.find_element(By.XPATH, "//a[text()='Women']").click()

print("success")

# time.sleep(2)
# driver.close()