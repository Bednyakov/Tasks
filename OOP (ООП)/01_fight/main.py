import random

class Warrior:
    def __init__(self, name, health=100, power=20):
        self.name = name
        self.health = health
        self.power = power

def duel(warrior_1, warrior_2):
    print('Дуэль началась:\n')
    while warrior_1.health > 0 and warrior_2.health > 0:
        hit = random.randint(1, 2)
        if hit == 1:
            hit = warrior_1
            warrior_2.health -= warrior_1.power
            print(f'{warrior_1.name}({warrior_1.health}) '
                  f'атаковал {warrior_2.name}({warrior_2.health}).')
        else:
            hit = warrior_2
            warrior_1.health -= warrior_2.power
            print(f'{warrior_2.name}({warrior_2.health}) '
                  f'атаковал {warrior_1.name}({warrior_1.health}).')
    print(f'\nПобеду одержал {hit.name}')

viking = Warrior('Викинг')
knight = Warrior('Рыцарь')

duel(viking, knight)
