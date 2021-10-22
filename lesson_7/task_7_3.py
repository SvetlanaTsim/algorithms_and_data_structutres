'''
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
'''

import random

m = int(input('Введите число: '))
arr = [random.randint(-100, 100) for i in range(2 * m + 1)]

'''Элемент является медианой, если количево элементов в списке, которые не больше его равно
 количетву не меньших по значению элементов, без учета самого элемента'''
for i in range(len(arr)):
    amount_min = 0
    amount_max = 0
    amount_eq = 0
    for j in range(len(arr)):
        if j != i:
            if arr[i] > arr[j]:
                amount_max += 1
            elif arr[i] < arr[j]:
                amount_min += 1
            else:
                amount_eq += 1
    if amount_min == amount_max == m \
            or amount_eq >= m\
            or (amount_min + amount_eq >= m and amount_min <= m) \
            or (amount_max + amount_eq >= m and amount_max <= m):
        med_num = arr[i]
        break

print(arr)
print(f'Медианный элемент по алгоритму решения: {med_num}')
#проверка
print(sorted(arr))
print(f'Правильный ответ: {sorted(arr)[m]}')
