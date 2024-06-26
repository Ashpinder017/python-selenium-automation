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

driver.get("http://www.target.com")

# driver.find_element(By.XPATH="//input[@id='search']")
driver.find_element(By.XPATH, "//input[@id='search']").click()
driver.find_element(By.XPATH, '//input[@id="search"]').send_keys('Toys')
driver.find_element(By.XPATH, "//button[@aria-label='search']").click()
sleep(5)
