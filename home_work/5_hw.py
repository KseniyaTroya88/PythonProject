# #1. Создайте функцию которая
# a. переходит на страницу https://www.saucedemo.com/
# b. находит элементы:
#  - текстовое поле username
#  - текстовое поле password
#  - кнопку submit
# c. Создайте условие, если элементы найдены - вывести в консоль текст “Элементы найдены”

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

try:
    driver.get("https://www.saucedemo.com/")

    # Селекторы для этого сайта
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    print("Все элементы найдены")

except NoSuchElementException:
    print("Ошибка: какой-то элемент не найден")
finally:
    driver.quit()