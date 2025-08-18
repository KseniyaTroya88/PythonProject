# #1. Создайте функцию которая
# a. переходит на страницу https://www.saucedemo.com/
# b. находит элементы:
#  - текстовое поле username
#  - текстовое поле password
#  - кнопку submit
# c. Создайте условие, если элементы найдены - вывести в консоль текст “Элементы найдены”

# Переход на страницу https://www.saucedemo.com/
# При отработке открывается сайт
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get ('https://www.saucedemo.com/')

username = driver.find_element(By.CSS_SELECTOR, '#user-name')
if username is None:
    print('Текстовое поле Username не найдено')
else:
    print('Текстовое поле Username найдено')

password = driver.find_element(By.CSS_SELECTOR, '#password')
if password is None:
    print('Текстовое поле Password не найдено')
else:
    print('Текстовое поле Password найдено')

submit_button = driver.find_element(By.CSS_SELECTOR, '#login-button')
if submit_button is None:
    print('Кнопка Submit не найдена')
else:
    print('Кнопка Submit найдена')

# Результаты теста: Открылся браузер, далее, прошли проверки наличия текстовых полей и кнопки.
# Текстовое поле Username найдено
# Текстовое поле Password найдено
# Кнопка Submit найдена
