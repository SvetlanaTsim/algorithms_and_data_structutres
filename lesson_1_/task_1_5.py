'''
5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
'''
import string

letter_1, letter_2 = input('Введите две буквы ОТ "a" какой и ДО "z": ').split()

letter_list = list(string.ascii_lowercase)
idx_1 = letter_list.index(letter_1.lower())
idx_2 = letter_list.index(letter_2.lower())
chosen_letters = letter_list[idx_1+1: idx_2] if idx_2 > idx_1 else letter_list[idx_2+1: idx_1]

print(f'Между указанными буквами находятся следующие буквы: {chosen_letters}, количество букв: {len(chosen_letters)}')