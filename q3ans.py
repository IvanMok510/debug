from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://localhost:8000")

# Longer timeout matching the dynamic load time
wait = WebDriverWait(driver, 5)
element = wait.until(EC.visibility_of_element_located((By.ID, "dynamic-content")))
print("Dynamic content visible:", element.text)

driver.quit()
