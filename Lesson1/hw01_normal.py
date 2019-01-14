import math

__author__ = 'Николаев Иван'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

num = int(input('Введите произвольное число: '))
max = 0
maybe_max = 0
if num < 10:
    max = num
else:
    while True:
        if num > 10:
            maybe_max = num % 10
            num = num // 10
            if max < maybe_max:
                max = maybe_max
        else:
            if max < num:
                max = num
            break
print(max)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

a = int(input('Введите значение переменной a: '))
b = int(input('Введите значение переменной b: '))
b = a + b
a = b - a
b = b - a
print('Теперь значение переменной a равно', a, ', а значение переменной b равно', b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

print('Дано уравнение вида ax² + bx + c = 0')
a = int(input('Введите значение коэффициента a: '))
b = int(input('Введите значение коэффициента b: '))
c = int(input('Введите значение коэффициента c: '))
D = (b ** 2) - (4 * a * c)
if D < 0:
    print('Нет корней')
elif D == 0:
    x1 = ((-b) + math.sqrt(D)) / (2 * a)
    print('Корень x1 равен: ', x1)
else:
    x1 = ((-b) + math.sqrt(D)) / (2 * a)
    x2 = ((-b) - math.sqrt(D)) / (2 * a)
    print('Корень x1 равен: ', x1)
    print('Корень x2 равен: ', x2)