import math

print('Введите координаты монетки: ')
x = float(input('X: '))
y = float(input('Y: '))
r = float(input('Введите радиус: '))

def coin(x,y,r):
    if math.sqrt(x * x + y * y) <= r:
        print('\nМонетка где-то рядом.')
    else:
        print('\nМонетки в области нет.')

coin(x,y,r)