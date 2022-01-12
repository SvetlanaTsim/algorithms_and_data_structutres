'''
Определить количество различных подстрок с использованием хеш-функции.
Задача: на вход функции дана строка, требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
'''

import hashlib


def get_substr_count(str='she sells seashells on the seahore'):
    h_str = hashlib.sha1(str.encode('utf-8')).hexdigest()
    sub_set = set()
    for i in range(len(str)):
        for j in range(len(str), i, -1):
            sub_str = str[i: j]
            h_sub = hashlib.sha1(sub_str.encode('utf-8')).hexdigest()
            if h_sub != h_str:
                sub_set.add(h_sub)
    return len(sub_set)


sub_str_num = get_substr_count(
    'my bonny lies over the ocean my bonny lies over the sea my bonny lies over the ocean oh bring back my bonny to me')
print(f'Количество подстрок в строке = {sub_str_num}')
