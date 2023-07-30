from random import randint, choice

class Karma:
    def __init__(self):
        self.__karma_points = 0
        self.__days_count = 0

    def one_day(self, value):
        self.set_day()
        try:
            if value == 10:
                exepts_tuple = ('KillError', 'DrunkEror', 'CarCrashError', 'GluttonyError', 'DepressionError')
                raise Exception(choice(exepts_tuple))
            else:
                point = randint(1, 7)
                self.set_karma_point(point)
        except Exception as exc:
            with open('karma.log', 'a', encoding='UTF-8') as file:
                file.writelines(f'\nДень {self.get_day()}, ошибка: {exc}')

    def set_karma_point(self, point):
        self.__karma_points += point

    def get_karma(self):
        return self.__karma_points

    def get_day(self):
        return self.__days_count

    def set_day(self):
        self.__days_count += 1

    def toconstant(self):
        while True:
            finish = self.get_karma()
            if finish >= 500:
                print(f'День {self.get_day()}, набрано {finish} очков кармы.')
                break
            else:
                value = randint(1, 10)
                self.one_day(value)

gokarma = Karma()
gokarma.toconstant()

