from random import randint

class Homo:
    def __init__(self, name, home, hungry=50):
        self.name = name
        self.hungry = hungry
        self.home = home

    def eating(self):
        if self.home.food > 0:
            self.home.food -= 1
            self.hungry += 1

    def shoping(self):
        if self.home.money > 0:
            self.home.money -= 1
            self.home.food += 1
        else:
            self.working()

    def working(self):
        self.home.money += 1
        self.hungry -= 1

    def gaming(self):
        self.hungry -= 1

    def die(self):
        if self.hungry < 0:
            return True

    def action(self):
        act = randint(1, 6)
        if self.hungry < 20:
            self.eating()
        elif self.home.food < 10:
            self.shoping()
        elif self.home.money < 50:
            self.working()
        elif act == 1:
            self.working()
        elif act == 2:
            self.eating()
        elif act in (3, 4, 5, 6):
            self.gaming()

    def info(self):
        print(f'{self.name} голод: {self.hungry}')

class Home:
    def __init__(self, food=50, money=0):
        self.food = food
        self.money = money

    def info(self):
        print(f'Запасы в доме: еда({self.food}), деньги({self.money})')

def sim(p1, p2):
    day = 0
    while day != 365:
        if p1.die() is not True and p2.die() is not True:
            day += 1
            p1.action()
            p2.action()
        else:
            print(f'Один из персонажей умер')
            break
    print(f'Персонажи прожили {day} дней.\n')

sweet_home = Home()
person_1 = Homo('Bob', sweet_home)
person_2 = Homo('Alexa', sweet_home)

sim(person_1, person_2)
sweet_home.info()
person_1.info()
person_2.info()
