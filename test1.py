from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver.maximize_window()
driver = webdriver.Chrome(ChromeDriverManager())
driver.get('https://wwww.amazon.com')

driver.find_element((By.ID,"input[@aria-label='Search Amazon']"))


driver.find_element(By.XPATH,"//select[@aria-describedby='searchDropdownDescription']")
