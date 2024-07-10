from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    browser = webdriver.Chrome()
    browser.get('https://SunInJuly.github.io/execute_script.html')

    s = str(math.log(abs(12*math.sin(int(browser.find_element(By.ID, 'input_value').text)))))
    browser.find_element(By.ID, 'answer').send_keys(s)

    browser.find_element(By.ID, 'robotCheckbox').click
    browser.find_element(By.ID, 'robotsRule').location_once_scrolled_into_view
    browser.find_element(By.ID, 'robotsRule').click()

    browser.find_element(By.CLASS_NAME, "btn").click()

finally:
    time.sleep(10)
    browser.quit()