
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ser_obj = Service("Selenium Drivers/chromedriver_win32/chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = options, service = ser_obj)
driver.get("https://admin-demo.nopcommerce.com/login")

elem = driver.find_element(By.ID, "Email")
elem.clear()
elem.send_keys("admin@yourstore.com")


elem = driver.find_element(By.ID, "Password")
elem.clear()
elem.send_keys("admin")

elem = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button")
elem.click()

act_title = driver.title
exp_title = "Dashboard / nopCommerce administration"
# print(act_title)

if act_title == exp_title :
    print("Login test Passed")
else :
    print("Login test Failed")

driver.close()