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


print("success")