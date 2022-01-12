'''
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
'''
import random
chance_num = [random.randint(-100, 100) for i in range(100)]

max = float("-inf")
for num in chance_num:
    if num < 0:
        if num > max:
            max = num

print(chance_num)
print(f'Маскимальное отрицательное число в списке = {max}, позиция в списке {chance_num.index(max)}')
