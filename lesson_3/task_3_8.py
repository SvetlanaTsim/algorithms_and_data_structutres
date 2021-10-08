'''
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
'''
def get_matrix(n, m):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            a = float(input(f'Введите число ряда {i+1}: '))
            row.append(a)
        row.append(sum(row))
        matrix.append(row)
    return matrix

if __name__ == '__main__':
    print(get_matrix(5,4))
