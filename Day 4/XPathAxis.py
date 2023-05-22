import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("Selenium Drivers/chromedriver_win32/chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=serv_obj, options=options)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

# 1. self (//tagname[attribute, value]/self::tagname)

# text_msg = driver.find_element(By.XPATH, "//a[contains(text(), 'Muthoot Finance')]/self::a").text
# print(text_msg) # Muthoot Finance

# 2. parent (//tagname[attribute, value]/parent::tagname)

# text_msg = driver.find_element(By.XPATH, "//a[contains(text(), 'Muthoot Finance')]/parent::td").text
# print(text_msg) # Muthoot Finance

# 3. Child (//tagname[attribute, value]/ancestor::tagname/child::tagname)

# text_msg = driver.find_elements(By.XPATH, "//a[contains(text(), 'Muthoot Finance')]/ancestor::tr/child::td")
# print(text_msg) # Muthoot Finance

# 4 .Ancestor (//tagname[attribute, 'value']/ancestor::tagname)

# ancestor = driver.find_element(By.XPATH, "//a[contains(text(), 'Muthoot Finance')]/ancestor::tr").text
# print(ancestor) # Muthoot Finance A 1,034.75 1,125.00 + 8.72

# 5. Descendant (//tagname[attribute, 'value']/ancestor::tagname/descendant::tagname)

# descendent = driver.find_elements(By.XPATH, "//a[contains(text(), 'Muthoot Finance')]/ancestor::tr/descendant::*")
# print(len(descendent))  # 7

# 6. Following (//tagname[attribute, 'value']/ancestor::tagname/following::tagname)

# following = driver.find_elements(By.XPATH, "//a[contains(text(), 'Muthoot Finance')]/ancestor::tr/following::*")
# print(len(following))  # 3052

# 7. Following-sibling (//tagname[attribute, 'value']/ancestor::tagname/following-sibling::tagname)

# followingSibling = driver.find_elements(By.XPATH, "//a[contains(text(), 'Muthoot Finance')]/ancestor::tr/following-sibling::tr")
# print(len(followingSibling))  # 360

# 8. Preceding (//tagname[attribute, 'value']/ancestor::tagname/preceding::tagname)

# preceding = driver.find_elements(By.XPATH, "//a[contains(text(), 'Muthoot Finance')]//ancestor::tr/preceding::tr")
# print(len(preceding))  # 8

# 9. Preceding-sibling (//tagname[attribute, 'value']/ancestor::tagname/preceding-sibling::tagname)

precedingSibling = driver.find_elements(By.XPATH, "//a[contains(text(), 'Muthoot Finance')]//ancestor::tr/preceding-sibling::tr")
print(len(precedingSibling))  # 7


# time.sleep(2)
driver.close()