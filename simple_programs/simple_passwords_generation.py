# -*- coding: utf8 -*-
from random import *
from string import *


symbols = list((set(ascii_letters) | set(digits)) - set('lI1oO0'))  # коллекция символов без схожих по внешнему виду


def generate_password(length):  # функция генерации пароля с длиной length
    password = []
    while True:
        check_upper, check_lower, check_digits = False, False, False  # флаги для проверки того, что в пароле есть цифра
        # , прописная и строчная буквы
        for _ in range(length):
            password.append(choice(symbols))  # добавляем в пароль случайный символ
            if len(password) == length:  # проверяем принадлежность символов к требуемым наборам
                for i in password:
                    if i in digits:
                        check_digits = True
                    elif i in ascii_uppercase:
                        check_upper = True
                    elif i in ascii_lowercase:
                        check_lower = True
        if len(password) == length and check_upper and check_lower and check_digits:  # условие для возвращения пароля
            return ''.join(password)
        else:
            password.clear()  # делаем заново, если условие не выполнено
            continue


n, m = int(input()), int(input())

for _ in range(n):  # выводим пароли в нужном количестве
    print(generate_password(m))

