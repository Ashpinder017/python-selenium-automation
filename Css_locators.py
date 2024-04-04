from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

#driver.get(https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_custrec_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
driver.get("https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_custrec_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

driver.find_element(By.CSS_SELECTOR, "[aria-label='Amazon']")
driver.find_element(By.CSS_SELECTOR, "h1[class*='a-spacing-small']")
sleep(2)
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, "input#ap_email").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, "#ap_password").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, "#continue")

driver.find_element(By.XPATH,"//a[text()='Conditions of Use']")
driver.find_element(By.XPATH,"//a[text()='Privacy Notice']")
expected="Sign in"
actual=driver.find_element(By.CSS_SELECTOR, "[class*='a-link-emphasis'").text

assert expected == actual,f'{expected} != {actual}'

sleep(5)
