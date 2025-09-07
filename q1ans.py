from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://localhost:8000")

# Correct ID with a wait to ensure page load
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "click-me")))
element.click()

print("Element clicked successfully!")
driver.quit()
