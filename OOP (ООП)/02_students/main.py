class Student:
    def __init__(self, name, group, progress):
        self.name = name
        self.group = group
        self.progress = progress

    def info(self):
        print(f'Студент: {self.name} | Группа: {self.group} | Ср. балл: {self.middle()}')

    def middle(self):
        count = 0
        mid = 0
        for i in self.progress:
            count += 1
            mid += i
        mid = round((mid / count), 1)
        return mid

def sortedstudents(list_of_students):
    sorted_list = sorted(list_of_students, key=lambda elem: elem.middle())
    for stud in sorted_list:
        stud.info()

stud_list = [Student('Bob', '2F', [5, 4, 5, 3, 3]),
             Student('Mike', '2F', [4, 4, 4, 3, 2]),
             Student('Mila', '2F', [3, 2, 3, 2, 2]),
             Student('Bill', '2A', [3, 3, 3, 2, 2]),
             Student('John', '2A', [3, 3, 1, 2, 2]),
             Student('Jacob', '2A', [3, 4, 4, 4, 2]),
             Student('Victor', '2C', [3, 3, 1, 2, 2]),
             Student('Natasha', '2C', [2, 2, 3, 2, 2]),
             Student('Ella', '2C', [3, 5, 5, 2, 2])]

sortedstudents(stud_list)


