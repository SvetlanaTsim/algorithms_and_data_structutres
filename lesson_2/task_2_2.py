'''
2. Посчитать четные и нечетные цифры введенного натурального числа.
 Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''

num = input('Введите натуральное число: ')

even_num = [i for i in list(map(int, list(num))) if i % 2 == 0]
odd_num = [i for i in list(map(int, list(num))) if i % 2 != 0]

print(f'Четные:{even_num}, количество: {len(even_num)}')
print(f'Нечетные:{odd_num }, количество: {len(odd_num )}')
