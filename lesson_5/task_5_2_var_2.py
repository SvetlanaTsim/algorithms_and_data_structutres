class HexNum:
    def __init__(self, num):
        self.num = list(num.upper())

    def __str__(self):
        return str(list(self.num))

    def __add__(self, other):
        return list(str(hex(int(''.join(self.num), 16) + int(''.join(other.num), 16)).upper()))[2:]

    def __mul__(self, other):
        return list(str(hex(int(''.join(self.num), 16) * int(''.join(other.num), 16)).upper()))[2:]


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