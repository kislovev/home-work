# Задание 2. Реализовать с помощью цикла while
# Последовательность чисел трибоначчи задается рекуррентным соотношением:
# F(1) = 0
# F(2) = 1
# F(3) = 1
# F(n) = F(n–3) + F(n–2) + F(n–1), при n >3, где n – натуральное число.
# Чему равно девятое число в последовательности трибоначчи? (ответ 44)


Fn = [0, 1, 1]
n = 44
while len(Fn) < n:
    Fn.append(Fn[-1] + Fn[-2] + Fn[-3])
    if Fn[:n] == n:
        break
print(Fn)

