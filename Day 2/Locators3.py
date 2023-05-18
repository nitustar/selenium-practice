from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("Selenium Drivers/chromedriver_win32/chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=serv_obj, options=options)

driver.get("https://www.facebook.com/")
driver.maximize_window()

# Tag and ID (Syntax -> 'tag#id' where tag is "optional")

# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc")

# Tag and Class (Syntax -> "tag.valueOfClass" where tag is 'optional')

# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abcd")
# driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("abcdes")

# Tag and Attribute (Syntax -> "tag[Attribute = value]" where tag is optional)

# driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("happysingh")
# driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("happysingh")

# Tag and Class and Attribute (Syntax -> "tag.valueOfClass[attribute = value]" where tag is optional)

# driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_email]").send_keys("abcdefgh")
driver.find_element(By.CSS_SELECTOR, ".inputtext[data-testid=royal_email]").send_keys("abcdefgh")

driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass]").send_keys("xyz")