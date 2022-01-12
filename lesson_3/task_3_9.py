'''
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''

from task_3_8 import *

matrix = get_matrix(5,4)

min_list = []
for j in range(len(matrix[0])):
    row = []
    for i in matrix:
        row.append(i[j])
    min_list.append(min(row))

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы = {max(min_list)}')
