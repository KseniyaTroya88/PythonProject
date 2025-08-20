# #1. Создайте функцию которая
# a. переходит на страницу https://www.saucedemo.com/
# b. находит элементы:
#  - текстовое поле username
#  - текстовое поле password
#  - кнопку submit
# c. Создайте условие, если элементы найдены - вывести в консоль текст “Элементы найдены”

from selenium import webdriver
from selenium.webdriver.common.by import By


def check_saucedemo_elements():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')

    # селекторы:
    username_list = driver.find_elements(By.CSS_SELECTOR, '#user-name')
    password_list = driver.find_elements(By.CSS_SELECTOR, '#password')
    submit_list = driver.find_elements(By.CSS_SELECTOR, '#login-button')

    if username_list:
        print('Текстовое поле Username найдено')
    else:
        print('Текстовое поле Username не найдено')

    if password_list:
        print('Текстовое поле Password найдено')
    else:
        print('Текстовое поле Password не найдено')

    if submit_list:
        print('Кнопка Submit найдена')
    else:
        print('Кнопка Submit не найдена')

    if username_list and password_list and submit_list:
        print("Элементы найдены")


check_saucedemo_elements()

# Результаты теста: Открылся браузер, далее, прошли проверки наличия текстовых полей и кнопки.
# Текстовое поле Username найдено
# Текстовое поле Password найдено
# Кнопка Submit найдена
# Элементы найдены
