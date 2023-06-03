with open('people.txt', 'w', encoding='UTF-8') as file:
    file.write('''Василий
Николай
Надежда
Никита
Ян
Ольга
Евгения
Кристина''')

with open('people.txt', 'r', encoding='UTF-8') as file, \
        open('errors.log', 'w', encoding='UTF-8') as log_file:
    count = 0
    num = 0

    for line in file:
        try:
            num += 1
            nice_line = line.rstrip()
            count += len(nice_line)
            if len(nice_line) < 3:
                raise BaseException
        except BaseException:
            print(f'Ошибка: в {num} строке менее трех символов.')
            log_file.write(f'Ошибка: в {num} строке менее трех символов.\n')

print(f'Общее количество символов: {count}')



