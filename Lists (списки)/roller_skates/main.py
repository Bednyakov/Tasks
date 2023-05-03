skates_list = []
humans_list = []

num_skates = int(input('\nКоличество коньков: '))
for i in range(num_skates):
    size = int(input(f'Размер {i + 1}-й пары: '))
    skates_list.append(size)

num_humans = int(input('\nКоличество людей: '))
for j in range(num_humans):
    size = int(input(f'Размер ноги {j + 1}-го человека: '))
    humans_list.append(size)

count = 0
for k in humans_list:
    if k in skates_list:
        count += 1
        skates_list.remove(k)


print(f'\nНаибольшее кол-во людей, которые могут взять ролики: {count}')
