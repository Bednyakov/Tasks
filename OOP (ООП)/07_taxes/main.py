from random import randint

class Unit:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.__power = 20
        self.__dead = False

    def __str__(self):
        return f'Юнит {self.name} имеет {self.health} HP.'


    def damage(self, obj):
        print(f'\n{self.name} нанес урон {obj.name}.')
        obj.health -= self.get_power()
        print(obj.__str__())
        obj.set_dead()

    def get_power(self):
        return self.__power

    def set_dead(self):
        if self.health <= 0:
            self.__dead = True

    def get_dead(self):
        return self.__dead

class Game:
    def __init__(self):
        self.__count = 0
        self.war1 = Unit('Викинг')
        self.war2 = Unit('Крестьянин')

    def battle(self):
        while True:
            if self.get_count() == 0:
                self.present()
                self.set_count()
            hit = randint(1, 2)
            if hit == 1:
                self.war1.damage(self.war2)
                if self.war2.get_dead() == True:
                    self.finish(self.war1)
                    break
            else:
                self.war2.damage(self.war1)
                if self.war1.get_dead() == True:
                    self.finish(self.war2)
                    break

    def present(self):
        print('\t\t\tДа начнется великая битва!')

    def set_count(self):
        self.__count += 1

    def get_count(self):
        return self.__count

    def finish(self, obj):
        print(f'Победил {obj.name}. Славная победа!')

game = Game()
game.battle()




