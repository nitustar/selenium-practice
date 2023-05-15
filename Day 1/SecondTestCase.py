
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ser_obj = Service("Selenium Drivers/chromedriver_win32/chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ser_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.implicitly_wait(2)

elem = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")
elem.clear()
elem.send_keys("Admin")


elem = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input")
elem.clear()
elem.send_keys("admin123")
#
elem = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
elem.click()

act_title = driver.title
exp_title = "OrangeHRM"
print(act_title)
if act_title == exp_title :
    print("Login test Passed")
else :
    print("Login test Failed")

driver.close()