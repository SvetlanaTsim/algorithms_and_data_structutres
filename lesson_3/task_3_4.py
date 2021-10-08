'''
Определить, какое число в массиве встречается чаще всего.
'''

import random
chance_num = [random.randint(1, 100) for _ in range(100)]

max_count = 0
for i in chance_num:
    if chance_num.count(i) > max_count:
        max_count = i

print(chance_num)
print(f'Чаще всего встречается в списке число {max_count}, встречается {chance_num.count(max_count)} раз' )
