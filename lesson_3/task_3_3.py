'''
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
import random
# чтобы были уникальные
chance_num = list(set([random.randint(1, 100) for _ in range(100)]))

print(chance_num)

a = chance_num.index(min(chance_num))
b = chance_num.index(max(chance_num))

chance_num[a], chance_num[b] = chance_num[b], chance_num[a]
print(chance_num)
