from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


def func(link):
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, "//label[text()='First name*']/following::input[1]")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//label[text()='Last name*']/following::input[1]")
    input2.send_keys("Petrov")
    input2 = browser.find_element(By.XPATH, "//label[text()='Email*']/following::input[1]")
    input2.send_keys("Petrov")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # закрываем браузер после всех манипуляций
    browser.quit()
    return welcome_text

class TestPass(unittest.TestCase):
    def test_meth1(self):
        self.assertEqual(func('http://suninjuly.github.io/registration1.html'), "Congratulations! You have successfully registered!")

    def test_meth2(self):
        self.assertEqual(func('http://suninjuly.github.io/registration2.html'), "Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()