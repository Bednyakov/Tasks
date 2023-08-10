'''Класс-итератор'''
class Square:
    def __init__(self, stop):
        self.stop = stop
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count == self.stop + 1:
            raise StopIteration
        result = self.count ** 2
        return result

print('Метод 1: ')
square = Square(8)
for i in square:
    print(i, end=' ')
print('\n')

'''Функция-генератор'''

def square_func(num):
    count = 1
    for _ in range(num):
        if count <= num:
            yield count ** 2
        count += 1

print('\nМетод 2: ')
sqare_gen = square_func(num=8)
for i in sqare_gen:
    print(i, end=' ')
print('\n')

'''Генераторное выражение'''

print('\nМетод 3: ')

num = 8
res = (x ** 2 for x in range(1, num + 1))
for i in res:
    print(i, end=' ')





