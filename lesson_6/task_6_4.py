'''
1. Подсчитать, сколько было выделено памяти под переменные
в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов
кода для одной и той же задачи. Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

Python 3.9.4
Windows 10  64-разрядная ОС, процессор x64
'''

'''
2_4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
'''
import sys

def math_fucn(n):
    my_list = []
    for i in range(n):
        if i % 2 ==0:
            y = 1 /2 ** i
        else:
            y = -(1 / 2 ** i)
        my_list.append(y)
    return my_list, sum(my_list)

a, b = math_fucn(int(input()))

print(f'Список такой: {a}, сумма: {b}')

print(f'Размеры переменных следующие:\na {sys.getsizeof(a)}'
     f'\nb {sys.getsizeof(b)}')

'''
Результат:
Список такой: [1.0, -0.5, 0.25, -0.125, 0.0625], сумма: 0.6875
Размеры переменных следующие:
a 120
b 24
Получается, список из 5 дробных чисел занимает 120 байт, а одно дробное число 24 байта
'''