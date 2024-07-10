from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import p

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    # Ждем все элементы 5 секунд, проверяя каждые 0.5 сек
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ждем до 13 сек, пока цена не станет $100
    WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    browser.find_element(By.ID, "book").click()

    # Получаем x отправляем решенную задачу 
    browser.find_element(By.ID, 'answer').send_keys(calc(browser.find_element(By.ID, 'input_value').text))
    browser.find_element(By.ID, "solve").click()

    # Из модального окна парсим текст и получаем ответ
    alert_text = browser.switch_to.alert.text
    answer = alert_text.split(': ')[-1]
    browser.switch_to.alert.accept()

    # Логинимся в Stepik, обновляем страницу
    browser.get('https://stepik.org/catalog?auth=login')
    browser.find_element(By.ID, 'id_login_email').send_keys('kuuhaku112121@gmail.com')
    browser.find_element(By.ID, 'id_login_password').send_keys(p.p)
    browser.find_element(By.CLASS_NAME, 'sign-form__btn').click()
    browser.refresh()

    # Переходим ну страницу нужной задачи, вписываем ответ и отправляем
    browser.get('https://stepik.org/lesson/181384/step/8?unit=156009')
    browser.find_element(By.CLASS_NAME, 'ember-text-area').send_keys(answer)
    browser.find_element(By.CLASS_NAME, 'submit-submission').click()

finally:
    time.sleep(10)
    browser.quit()