from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import p

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    browser.find_element(By.CLASS_NAME, "btn").click()
    browser.switch_to.window(browser.window_handles[1])

    browser.find_element(By.ID, 'answer').send_keys(calc(browser.find_element(By.ID, 'input_value').text))
    browser.find_element(By.CLASS_NAME, "btn").click()

    alert_text = browser.switch_to.alert.text
    answer = alert_text.split(': ')[-1]
    browser.switch_to.alert.accept()

    browser.get('https://stepik.org/catalog?auth=login')
    browser.find_element(By.ID, 'id_login_email').send_keys('kuuhaku112121@gmail.com')
    browser.find_element(By.ID, 'id_login_password').send_keys(p.p)
    browser.find_element(By.CLASS_NAME, 'sign-form__btn').click()
    browser.refresh()

    browser.get('https://stepik.org/lesson/184253/step/6?unit=158843')
    browser.find_element(By.CLASS_NAME, 'ember-text-area').send_keys(answer)
    browser.find_element(By.CLASS_NAME, 'submit-submission').click()

finally:
    time.sleep(10)
    browser.quit()