from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("Selenium Drivers/chromedriver_win32/chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=serv_obj, options=options)

driver.get("https://automationpractice.pl/index.php")
driver.maximize_window()

# CLASS_NAME Locators
# sliders = driver.find_elements(By.CLASS_NAME, "homeslider-container")
# print("Number of Sliders: ", len(sliders))

# TAG_NAME Locators
links = driver.find_elements(By.TAG_NAME, "a")
print("Total links in the page: ", len(links))

driver.close()