# Задача 1. Создайте класс прямоугольника.
# a. атрибуты - прямоугольнику можно задать ширину и высоту
# b. методы - реализуйте 2 метода:
# - расчет площади прямоугольника
# - расчет периметра прямоугольника
# c. создайте 3 объекта, рассчитайте площадь и периметр для каждого.
# Результаты выводить в консоль.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        """Расчет площади прямоугольника"""
        return self.width * self.height

    def calculate_perimeter(self):
        """Расчет периметра прямоугольника"""
        return 2 * (self.width + self.height)


# Создаем 3 объекта прямоугольников
rect1 = Rectangle(18, 4)
rect2 = Rectangle(8, 7)
rect3 = Rectangle(4, 10)

# Рассчитываем и выводим результаты для каждого
print(f"Прямоугольник 1: ширина={rect1.width}, высота={rect1.height}")
print(f"Площадь: {rect1.calculate_area()}")
print(f"Периметр: {rect1.calculate_perimeter()}\n")

print(f"Прямоугольник 2: ширина={rect2.width}, высота={rect2.height}")
print(f"Площадь: {rect2.calculate_area()}")
print(f"Периметр: {rect2.calculate_perimeter()}\n")

print(f"Прямоугольник 3: ширина={rect3.width}, высота={rect3.height}")
print(f"Площадь: {rect3.calculate_area()}")
print(f"Периметр: {rect3.calculate_perimeter()}")


# Задача 2. Создайте класс Math.
# a. Создайте два атрибута — a и b.
# b. Напишите методы
# - addition — сложение,
# - multiplication — умножение,
# - division — деление,
# - subtraction — вычитание.
# При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        """Сложение a и b"""
        result = self.a + self.b
        print(f"Сложение: {self.a} + {self.b} = {result}")

    def multiplication(self):
        """Умножение a на b"""
        result = self.a * self.b
        print(f"Умножение: {self.a} * {self.b} = {result}")

    def division(self):
        """Деление a на b"""
        if self.b == 0:
            print("Ошибка: деление на ноль!")
        else:
            result = self.a / self.b
            print(f"Деление: {self.a} / {self.b} = {result}")

    def subtraction(self):
        """Вычитание b из a"""
        result = self.a - self.b
        print(f"Вычитание: {self.a} - {self.b} = {result}")


# Пример использования
math_ops = Math(18, 4)

math_ops.addition()  # 18 + 4 = 22
math_ops.multiplication()  # 18 * 4 = 72
math_ops.division()  # 18 / 4 = 4.5
math_ops.subtraction()  # 18 - 4 = 14

# Проверка деления на ноль
math_zero = Math(18, 0)
math_zero.division()  # Ошибка: деление на ноль!


# Задача 3. откройте страницу https://demoqa.com/text-box
# На странице присутствует сайдбар (меню слева)
# a. Создайте объекты для каждой кнопки 2-го уровня вложенности (“Text Box” и т.п.)
# Для этого опишите класс.
# Каждый объект должен содержать в себе:
# - текст кнопки (пример: “Text Box”)
# - тип - одинаковый для всех “Кнопка”
# - локатор - не заполнять, сделать по умолчанию пустой строкой
# Также на кнопку можно нажать - реализуйте метод. Метод возвращает текст “Клик по кнопке { ТЕКСТ КНОПКИ }”
# b. выведите текст для каждой кнопки
# c. вызовите “Клик” для каждой кнопки

class SidebarButton:
    def __init__(self, text):
        self.text = text
        self.type = "Кнопка"
        self.locator = ""

    def click(self):
        return f"Клик по кнопке {self.text}"


# Создаем объекты для всех кнопок 2-го уровня
buttons = [
    SidebarButton("Text Box"),
    SidebarButton("Check Box"),
    SidebarButton("Radio Button"),
    SidebarButton("Web Tables"),
    SidebarButton("Buttons"),
    SidebarButton("Links"),
    SidebarButton("Broken Links - Images"),
    SidebarButton("Upload and Download"),
    SidebarButton("Dynamic Properties")
]

# Выводим информацию о кнопках и имитируем клик
for button in buttons:
    print(f"Текст: {button.text}")
    print(f"Тип: {button.type}")
    print(f"Локатор: {button.locator}")
    print(button.click())
    print("-" * 30)  # Разделитель между кнопками