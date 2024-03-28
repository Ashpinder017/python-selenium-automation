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

driver.get("https://www.target.com")
driver.find_element(By.XPATH,"//span[@class='styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3']").click()

driver.find_element(By.XPATH,"//span[@class='styles__ListItemText-sc-diphzn-1 jaMNVl' and text()='Sign in']").click()

title=driver.title
print(title)
#driver.find_element(By.XPATH,"//span[text()='Sign into your Target account']")
sleep(2)
page_url = driver.current_url
print("You are on page:",page_url)
driver.find_element(By.XPATH,"//input[@id='username']").click()
driver.find_element(By.XPATH,"//input[@id='username']").send_keys("newuser")
sleep(5)
driver.find_element(By.XPATH,"//input[@id='password']").click()
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("<PASSWORD@1>")
sleep(7)
driver.find_element(By.XPATH,"//button[@type='submit']")

