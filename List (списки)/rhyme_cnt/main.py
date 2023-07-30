humans = int(input('Количество человек: '))
humans_list = list(range(1, humans + 1))
num = int(input('Какое число в считалке: '))
print(f'Значит выбывает каждый {num}-й человек.')
start = 0

while len(humans_list) != 1:
    print(f'\nТекущий круг людей: {humans_list}')
    index = start % len(humans_list)
    print(f'Начало счета с {humans_list[index]} человека.')
    start = (index + num - 1) % len(humans_list)
    print(f'Выбывает человек под номером {humans_list[start]}.')
    humans_list.remove(humans_list[start])

print('\nОстался человек под номером ', *humans_list)





