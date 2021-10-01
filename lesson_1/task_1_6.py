'''
6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
'''

import string

letter_num = int(input('Введите номер буквы в алфавите"a" какой и ДО "z": '))

letter_list = list(string.ascii_lowercase)

print(f'Это буква: {letter_list[letter_num-1]}')
