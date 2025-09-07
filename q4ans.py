from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://localhost:8000")

# Wait for visibility and interactability
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, "dynamic-content")))
# Scroll to it if needed
driver.execute_script("arguments[0].scrollIntoView(true);", element)
element.click()

print("Element interacted with successfully!")
driver.quit()
