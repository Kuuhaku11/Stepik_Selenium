import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')

    for i in browser.find_elements(By.CLASS_NAME, 'form-control'):
        i.send_keys('a')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    browser.find_element(By.CLASS_NAME, "btn").click()

finally:
    time.sleep(10)
    browser.quit()