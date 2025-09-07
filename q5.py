# 5. UnexpectedAlertPresentException (Unhandled Alerts)
# Description: An alert/pop-up appears, blocking further actions, but it's not handled.
# Common Causes: JavaScript alerts, confirms, or prompts triggered by actions.
# Debugging Tips: Switch to the alert with driver.switch_to.alert and accept/dismiss it. Check for alerts before proceeding.
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost:8000")

# Trigger alert but don't handle it
button = driver.find_element(By.XPATH, "//button[contains(text(), 'Trigger Alert')]")
button.click()

# Next action fails due to unhandled alert
input_field = driver.find_element(By.ID, "text-input")
input_field.send_keys("Text")  # Raises UnexpectedAlertPresentException

driver.quit()
