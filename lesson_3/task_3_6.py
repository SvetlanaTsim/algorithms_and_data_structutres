'''
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
 Сами минимальный и максимальный элементы в сумму не включать.
'''
import random
chance_num = [random.randint(-100, 100) for i in range(100)]
a = chance_num.index(max(chance_num))
b = chance_num.index(min(chance_num))
if a < b:
    new_list = chance_num[a + 1: b]
else:
    new_list = chance_num[b + 1: a]
print(chance_num)
print(f'Елементы между максимальным и минимальным: {new_list}, их сумма = {sum(new_list)}')
