from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

#Initialize
driver=webdriver.Chrome()

#Opening a webpage
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
sleep(4)

#Credentials
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")

#Log In-
sleep(1)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
sleep(4)

#Verify-
title=driver.title
print("driver Title from Webpage:",driver.title)
assert "OrangeHRM" == driver.title