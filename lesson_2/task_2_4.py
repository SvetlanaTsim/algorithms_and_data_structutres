'''
4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
'''
num_list = []

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
