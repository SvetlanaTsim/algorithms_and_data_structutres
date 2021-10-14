'''
1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
 Программа должна определить среднюю прибыль (за год для всех предприятий)
 и вывести наименования предприятий, чья прибыль выше среднего и отдельно
 вывести наименования предприятий, чья прибыль ниже среднего.
'''
from decimal import Decimal
from collections import defaultdict

firm_data = defaultdict(Decimal)
n = int(input('Введите сколько фирм: '))

for i in range(n):
    name = input('Введите название фирмы: ')
    profit = map(Decimal, (input('Введите прибыль фирмы за 4 квартала (4 числа подряд): ').split()))
    firm_data[name] = sum(profit)

avg_prof = round(sum(firm_data.values())/n, 2)

less_avg = [key for key, value in firm_data.items() if value < avg_prof]
more_avg = [key for key, value in firm_data.items() if value > avg_prof]
eq_avg = [key for key, value in firm_data.items() if value == avg_prof]

print(f'Введены данные {firm_data}')
print(f'Средний размер прибыли: {avg_prof}')
print(f'Прибыль выше среднего у предприятий: {more_avg}, ниже у: {less_avg}')
print(f'Прибыль равна средней у фирм(ы): {eq_avg}' if eq_avg else 'Cпасибо за внимание!')
