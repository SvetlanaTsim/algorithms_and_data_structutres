'''
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
'''
import random

chance_num = [random.randint(-100, 100) for i in range(100)]
chance_num.sort()
print(f'Два наименьших элемента: {chance_num[:2]}')
