'''
6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
'''

import random

num = random.randint(1,100)
attempt = 1
while True:
    if attempt >= 10:
        print(f'Попытки закончились! Правильный ответ {num}')
        break
    user_num = int(input('Угадайте целое число от 1 до 100: '))
    if user_num == num:
        print('Правильно!')
        break
    elif user_num > num:
        print('Ваше число больше загаданного!')
    else:
        print('Ваше число меньше загаданного!')
    attempt+=1
