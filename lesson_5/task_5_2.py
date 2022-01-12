'''
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections
'''
class HexNum:
    def __init__(self, num):
        self.num = num.upper()

    def __str__(self):
        return str(list(self.num))

    def __add__(self, other):
        return list(str(hex(int(self.num, 16) + int(other.num, 16)).upper()))[2:]

    def __mul__(self, other):
        return list(str(hex(int(self.num, 16)* int(other.num, 16)).upper()))[2:]


hex_1 = HexNum('A2')
hex_2 = HexNum('C4F')

hex_3 = HexNum(input('Введите шеснадцатеричное число: '))
hex_4 = HexNum(input('Введите шеснадцатеричное число: '))

print(hex_1)
print(hex_1 + hex_2)
print(hex_1 * hex_2)

print(hex_3)
print(hex_3 + hex_4)
print(hex_3 * hex_4)