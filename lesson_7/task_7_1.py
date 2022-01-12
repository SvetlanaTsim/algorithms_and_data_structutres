'''
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
'''
import random
import time

mas = [random.randint(-100, 100) for _ in range (10)]

def bubble_sort_decrease(mas):
    j = 1
    while j < len(mas):
        for i in range(len(mas) - j):
            if mas[i] < mas[i + 1]:
                mas[i], mas[i + 1] = mas[i + 1], mas[i]
        j += 1
    return mas
print(mas)
a = time.perf_counter()
print(bubble_sort_decrease(mas))
#Время работы алгоритма: 3.469999999999862e-05
print(f'Время работы алгоритма: {time.perf_counter() - a}')