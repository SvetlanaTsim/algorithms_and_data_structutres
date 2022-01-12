'''
1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''

big_list = [num for num in range(2, 100)]
shot_list = [num for num in range(2, 10)]

result_list = []
for num in big_list:
    for num_1 in shot_list:
        if num % num_1 == 0:
            result_list.append(num)

result_list = list(set(result_list))

if __name__ == '__main__':
    print(f'В диапазоне натуральных чисел от 2 до 99 кратны каждому из чисел в диапазоне'
          f' от 2 до 9 всего {len(result_list)} чисел, это числа: \n{result_list}')
