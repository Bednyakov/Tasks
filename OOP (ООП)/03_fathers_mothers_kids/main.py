class Parent:
    def __init__(self, name, age, child_list):
        self.name = name
        self.age = age
        self.child_list = child_list

    def info(self):
        print(f'''\nИмя: {self.name}
Возраст: {self.age}
Список детей: {[child.name for child in self.child_list]}''')

    def feeding(self, children):
        children.hunger += 1
    def lull(self, children):
        children.mood = True


class Children:
    def __init__(self, name, age, mood=False, hunger=0):
        self.name = name
        self.age = age
        self.mood = mood
        self.hunger = hunger

    def info(self):
        if self.mood == False:
            moodnow = 'Неспокоен'
        else:
            moodnow = 'Спокоен'
        if self.hunger < 3:
            hungernow = 'Голоден'
        else:
            hungernow = 'Сыт'
        print(f'''\nРебенок: {self.name}
Возраст: {self.age}
Состояние: {moodnow}
Сытость: {hungernow}''')

def interaction(parent, child_list):
    while True:
        print('\nСостояние детей:')
        for i in child_list:
            i.info()

        action = int(input(f'''\n1- Покормить {child_list[0].name}
2- покормить {child_list[1].name}
11- успокоить {child_list[0].name}
22- успокоить {child_list[1].name}
9 - информация о родителе
0 - выйти 
Введите нужное значение: '''))

        if action == 1:
            parent.feeding(child_list[0])
        if action == 11:
            parent.lull(child_list[0])
        if action == 2:
            parent.feeding(child_list[1])
        if action == 22:
            parent.lull(child_list[1])
        if action == 9:
            parent.info()
        if action == 0:
            print('\nПрограмма завершена.')
            break

chlist = [Children('Bob', 1), Children('Coralina', 8)]
mother = Parent('Luba', 28, chlist)

interaction(mother, chlist)

