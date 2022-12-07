# -*- coding: utf8 -*-
from string import digits, ascii_uppercase, ascii_lowercase

password = [i for i in input()]


def check_password():  # пароль должен быть длиной более 7 символов, иметь в себе хотя бы по одной цифре, заглавной и строчной букве
    return 'YES' if len(password) >= 7 and any(map(lambda x: x in ascii_lowercase, password)) and \
                    any(map(lambda x: x in ascii_uppercase, password)) and any(
        map(lambda x: x in digits, password)) else 'NO'


print(check_password())
