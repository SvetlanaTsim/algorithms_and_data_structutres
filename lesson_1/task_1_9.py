'''
9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
'''
a, b, c = map(float, input('Введите три числа: ').split())

if b < a < c or c < a < b:
   print(a)
elif a < b < c or c < b < a:
    print(b)
elif a < c < b or b < c < a:
    print(c)
else:
    print('Ошибка данных')