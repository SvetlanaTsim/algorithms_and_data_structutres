'''
7. Напишите программу, доказывающую или проверяющую,
 что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
'''

def first_part(n):
    if n == 1:
        return 1
    elif n > 0:
        return n + first_part(n - 1)
    else:
        return -1

def second_part(n):
    return n * (n + 1 ) // 2

n = 1
while True:
    if first_part(n) == second_part(n):
        print(f'Для n {n} - True')
    else:
        print(f'Для n {n} - False')
    n = n + 1