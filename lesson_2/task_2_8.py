'''
8. Посчитать, сколько раз встречается определенная
цифра в введенной последовательности чисел.
 Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
'''

seq = list(input('Введите последовательность чисел через пробел: '))
num = input('Введите цифру, которую нужно найти: ')

print(f'Цифра {num} встречается {seq.count(num)} раз')


