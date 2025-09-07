# 2. StaleElementReferenceException (Element No Longer Attached to DOM)
# Description: The element was found initially but becomes "stale" because the page refreshed or DOM changed (e.g., via JavaScript).
# Common Causes: AJAX updates, page navigations, or dynamic UI.
# Debugging Tips: Re-locate the element after changes. Use try-except to catch and retry. Avoid storing elements long-term; find them fresh each time.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8000")

# Find element before it's visible (dynamic content appears after 2s)
element = driver.find_element(By.ID, "dynamic-content")
time.sleep(1)  # Simulate some action that might refresh DOM
print(element.text)  # Might work initially, but if DOM changes, raises StaleElementReferenceException
driver.refresh()  # Force a refresh to trigger staleness
print(element.text)  # Now stale

driver.quit()
