# 4. ElementNotInteractableException (Can't Interact with Element)
# Description: Trying to click/type on an element that's not interactable, e.g., hidden or overlapped.
# Common Causes: Element not visible, disabled, or behind another element.
# Debugging Tips: Ensure visibility with waits. Scroll to the element using JavaScript. Check for overlays.
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost:8000")

# Try to interact with initially hidden dynamic content
element = driver.find_element(By.ID, "dynamic-content")
element.click()  # Raises ElementNotInteractableException

driver.quit()
