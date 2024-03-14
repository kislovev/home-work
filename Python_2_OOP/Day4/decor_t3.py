"""
Напишите функцию декоратор, которая переводит значение декорируемой функции
в рублях, в доллары (курс: 1$ = 69 рубля) или в евро (курс: 1€ = 73 руб).
Для тех, кто хочет добавить знак валюты:
chr(36) -> '$'
chr(8364) -> '€'
chr(8381) -> '₽'
chr(165) -> '¥'

Добавить возможность указать значок валюты для декоратора, по которому мы получаем значение.
"""

RATES = {
    "$": 90,
    "€": 98
         }


def exchange(arg):
    def real_func(func):
        def wrapper(*args, **kwargs):
            rub = float(func(*args, ** kwargs)[:-1])
            currency = RATES.get(arg)
            return f'{round(rub/currency, 2)}{arg}'
        return wrapper
    return real_func


@exchange("€")
def summa(count: float, price: float) -> str:
    return f'{round(count * price, 2)} р'


print(summa(100, 10))
