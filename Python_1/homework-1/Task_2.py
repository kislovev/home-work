# Задание 2. Дата некоторого дня характеризуется двумя натуральными числами: m (порядковый номер месяца) и n (число). По введенным m и n (в одну строку через пробел) определить:
# В задаче принять, что год не является високосным. Вывести предыдущую дату и следующую дату (в формате: mm.dd, где m - число месяца; d - номер дня) в одну строчку через пробел.
# P.S. Число дней в месяцах не високосного года, начиная с января: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

s31 = '1 3 5 7 8 12'.split()
s30 = '4 6 9 11'.split()
n = '3'

if n in s31:
    print("31")
elif n in s30:
    print('30')
else:
    print('28')