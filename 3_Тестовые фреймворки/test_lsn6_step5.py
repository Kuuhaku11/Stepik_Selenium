from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import p, time, math, pytest # type: ignore


@pytest.mark.parametrize('num', [895, 896, 897, 898, 899, 903, 904, 905])
def test_open(browser, num):

    browser.implicitly_wait(10)
    browser.get(f'https://stepik.org/lesson/236{num}/step/1')
    browser.find_element(By.CLASS_NAME, 'navbar__auth_login').click()
    browser.find_element(By.ID, 'id_login_email').send_keys('kuuhaku112121@gmail.com')
    browser.find_element(By.ID, 'id_login_password').send_keys(p.p)
    browser.find_element(By.CLASS_NAME, 'sign-form__btn').click()

    # answer = math.log(int(time.time() + 2.3))
    # time.sleep(2)
    # t = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'ember-text-area')))
    # t.send_keys(answer)
    # time.sleep(3)
    # button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission')))
    # button.click()
    # time.sleep(2)
    # corr = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
    # assert corr == 'Correct!'
    try:
        # Если кнопка "Решить снова" присутствует
        button3 = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.again-btn"))
        )
        button3.click()
        print('Кнопка "Решить снова" обнаружена, поле textarea неактивное')
        # Если кнопки "Решить снова" не оказалось
    except TimeoutException: # type: ignore
        print('Кнопка "Решить снова" не обнаружена, поле textarea активное')
        
    finally:
        # Ждем пока поле textarea не очистится и станет активным(пропадет атрибут "disabled"),
        # при этом не используем time.sleep!
        WebDriverWait(browser, 10).until_not(
        EC.element_attribute_to_include((By.CSS_SELECTOR, "textarea.ember-text-area"), 'disabled')
        )
        answer = math.log(int(time.time()))
        input3 = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.ember-text-area"))
        )
        input3.send_keys(answer)
        # Нажимаем кнопку "Отправить"
        button4 = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
        button4.click()
        # Ждем пока не появится фидбек, что ответ верный
        feedback = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint"))
        )
        #Сравниваем, что фидбек полностью совпадает с "Correct!"
        assert feedback.text == "Correct!", f"{feedback.text}"
