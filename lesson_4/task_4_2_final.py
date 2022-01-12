'''
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию:
Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.
'''
import math
import cProfile
from time import perf_counter

# Асимптотическая сложность: O(N), так как используется цикл
# Пространственная сложность: O(3) = O(1), так как создаем три переменные
def max_prime_num(i):
    ''' Функция для подсчета, до какого числа брать числовую прямую, чтобы найти нужное количество простых чисел.
    Функция основана на теореме о распределении простых чисел, которая утверждает, что
    количество простых чисел на отрезке[1;n] растёт с увеличением n как n / ln(n).
    '''
    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number

#Без использования «Решета Эратосфена»
# Асимптотическая сложность: O(N^2), так как дважды используется цикл
# Пространственная сложность: O(N^2), так как создается дважды список(второй раз копией)
def prime_without_eratosphen(i):
    primes = [2]
    number = 3
    while len(primes) < i:
        flag = True
        for j in primes.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            primes.append(number)
        number+=1
    return primes[-1]

#Используя алгоритм «Решето Эратосфена»
# Асимптотическая сложность: O(N log(log N)) + O(N)+ O(N) - потому что в конце создаем result_list и
# из-за вызова функции max_prime_num
# Пространственная сложность: O(2N), так как создается 2 списка
def prime_eratosphen(i):
    max_num = max_prime_num(i)
    numb = list(range(max_num+1))
    numb[0] = numb[1] = False
    for a in range(2, max_num):
        if numb[a]:
            for j in range(2 * a, max_num + 1, a):
                numb[j] = False
    result_list = [a for a in numb if a]
    return result_list[i-1]

t_1 = perf_counter()
print(prime_eratosphen(7))
t_2 = perf_counter()
print(f'Время выполение функции prime_eratosphen {t_2 - t_1}')

e_1 = perf_counter()
print(prime_without_eratosphen(7))
e_2 = perf_counter()
print(f'Время выполение функции prime_without_eratosphen {e_2 - e_1}')

'''
Комментарий: 
Время выполение функции prime_eratosphen 9.420000000000261e-05
Время выполение функции prime_without_eratosphen 3.5800000000002496e-05
Такая разница обусловлена включением дополнительной функции в prime_eratosphen
Убрала вызов функции, результат такой:
Время выполение функции prime_eratosphen 6.269999999999887e-05
Время выполение функции prime_without_eratosphen 2.1699999999999497e-05
'''

cProfile.run('prime_eratosphen(7)')
'''
        27 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_4_2_final.py:13(max_prime_num)
        1    0.000    0.000    0.000    0.000 task_4_2_final.py:45(prime_eratosphen)
        1    0.000    0.000    0.000    0.000 task_4_2_final.py:53(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       21    0.000    0.000    0.000    0.000 {built-in method math.log}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

cProfile.run('prime_without_eratosphen(7)')

'''

         41 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_4_2_final.py:28(prime_without_eratosphen)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       16    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        6    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
       15    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

