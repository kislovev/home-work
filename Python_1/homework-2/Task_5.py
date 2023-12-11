# Задание 3. Вводится натуральное число n. Необходимо сформировать список с помощью list comprehension, состоящий из делителей числа n (включая и само число n).
# Результат вывести на экран в одну строку через пробел.
# Входные данные:
# 10
# Выходные данные:
# 1 2 5 10
n = 10
# lst = []
# for i in range(1,n + 1):
#     if n % i == 0:
#         lst.append(i)
# print(lst)


lst = [i for i in range(1, n + 1) if n % i == 0]
lst_str = str(lst)
result = ' '.join(lst_str)
print(lst_str)
