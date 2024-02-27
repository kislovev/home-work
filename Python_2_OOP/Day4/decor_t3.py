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

rates = {
    '$': 90,
    '€': 98
}


def exchange(func: str):
    def wrapper(*args, **kwargs):
        change = {
            chr(36): 90,
            chr(8364): 100,
            chr(8381): 1,
            chr(165): 0.61
        }
        result = func(*args, **kwargs)
        currency = float(result[:-1]) / change.get(func)
        return f'{currency}{func}'
    return wrapper


@exchange(func= '€')
def summa(count: float, price: float) -> str:
    """ Out: <float><CHAR>"""
    return f'{round(count * price, 2)}₽'


print(summa(305.5, 2.4))
print(summa(1000, price=10))

