# Задание 3. Объявите функцию с именем check_password, которая принимает аргумент - строку (пароль)
# и имеет один формальный параметр chars с начальным значением в виде строки "$%!?@#". Функция должна проверять:
# есть ли в пароле хотя бы один символ из chars и что длина пароля  не менее 8 символов. Если проверка проходит,
# то функция возвращает True, иначе - False.

def check_password(password):
    chars = '$%!?@#'
    return True if password in chars and len(password) >= 8 else False


print(check_password('Ujh,fnjdf19'))
