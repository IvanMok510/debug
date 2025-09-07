from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8000")

# Wait for element, then re-find after potential DOM change
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.ID, "dynamic-content")))
print(element.text)

driver.refresh()  # Simulate DOM change
time.sleep(1)

# Re-find the element
element = wait.until(EC.visibility_of_element_located((By.ID, "dynamic-content")))
print(element.text)

driver.quit()
