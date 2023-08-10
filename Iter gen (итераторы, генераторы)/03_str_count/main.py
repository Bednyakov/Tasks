import os

# функция-генератор возвращающая количество строк
# во всех обнаруженных py файлах
def search_py_gen(dir: str='D:\Python'):

    for walktuple in os.walk(dir):
        for file in walktuple[2]:
            if file.endswith('.py'):
                pathfile = fR'{dir}\{file}'
                yield linecounter(pathfile)

# функция по подсчету строк в файле
def linecounter(path):
    count = 0
    with open(path, 'r', encoding='UTF-8') as file:
        while True:
            for line in file:
                if line[0] != '#' and line[0] != '\n':
                    count += 1
            return count

lines = search_py_gen()

for i in lines:
    print(i)

