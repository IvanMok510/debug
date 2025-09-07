# 3. TimeoutException (Waiting Too Long or Incorrect Conditions)
# Description: Selenium times out while waiting for an element or condition, e.g., during explicit waits.
# Common Causes: Slow network, incorrect wait conditions, or element never appears.
# Debugging Tips: Increase timeout duration. Use appropriate ExpectedConditions. Log wait attempts or use implicit waits as fallback.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://localhost:8000")

# Short timeout for dynamic element that takes 2s to appear
wait = WebDriverWait(driver, 1)  # Too short, raises TimeoutException
element = wait.until(EC.visibility_of_element_located((By.ID, "dynamic-content")))

driver.quit()
