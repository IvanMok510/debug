# 1. NoSuchElementException (Element Not Found)
# Description: Selenium can't locate an element on the page, often due to incorrect locators (e.g., ID, XPath, CSS) or the element not being present yet.
# Common Causes: Typos in locators, page not fully loaded, or dynamic elements.
# Debugging Tips: Use browser dev tools (F12) to inspect the element and verify the locator. Print the page source with print(driver.page_source) to check if the element exists. Add waits if the page is loading asynchronously.

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost:8000")

# Incorrect ID (typo)
element = driver.find_element(By.ID, "clickme")  # Raises NoSuchElementException
element.click()

driver.quit()
