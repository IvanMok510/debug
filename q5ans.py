from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://localhost:8000")

# Trigger alert and handle it
button = driver.find_element(By.XPATH, "//button[contains(text(), 'Trigger Alert')]")
button.click()

# Wait for and accept the alert
wait = WebDriverWait(driver, 10)
alert = wait.until(EC.alert_is_present())
alert.accept()

# Now proceed
input_field = driver.find_element(By.ID, "text-input")
input_field.send_keys("Text")
print("Text entered after handling alert!")

driver.quit()
