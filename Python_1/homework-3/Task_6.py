# Задача 1. Напишите функцию с именем get_rect_value,
# которая принимает два аргумента (два числа) и еще один формальный параметр type с начальным значением 0.
# Если параметр type равен нулю, то функция должна возвращать периметр прямоугольника, а иначе - его площадь.

def get_rect_value(x, y, type=0):
    if type == 0:
        return 2 * x + y
    else:
        return (x + y) / 2


print(get_rect_value(2, 4))


def get_rect_value(x, y, type=0):
    return 2 * x + y if type == 0 else (x + y) / 2


print(get_rect_value(2, 4, 1))
