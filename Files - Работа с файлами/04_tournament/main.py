# По умолчанию файла не было, я его создал по примеру README
#first_file = open('first_tour.txt', 'w', encoding='UTF-8')
#first_file.write('''80
#Ivanov Serg 80
#Sergeev Petr 92
#Petrov Vasiliy 98
#Vasiliev Maxim 78''')
#first_file.close()

first_file = open('first_tour.txt', 'r', encoding='UTF-8')
second_file = open('second_tour.txt', 'a', encoding='UTF-8')
win_list = []
start = int(first_file.readline())
for line in first_file:
    person = line.split()
    if int(person[2]) > start:
        new_person = ((person[1][0]), (person[0]), int(person[2]))
        win_list.append(new_person)

win_list.sort(key=lambda i:i[2], reverse=True)
second_file.write(f'{len(win_list)}\n')
for num, pers in enumerate(win_list, 1):
    second_file.write(f'{num}) {pers[0]}. {pers[1]} {pers[2]}\n')

first_file.close()
second_file.close()