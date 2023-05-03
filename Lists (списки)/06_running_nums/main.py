num_list = [1, 2, 3, 4, 5]
step = int(input('Сдвиг: '))
new_list = []
diff = len(new_list) - step

while step != 0:
    for _ in range(step):
        new_list.append(num_list[-step])
        step -= 1

for i in num_list[:diff]:
    new_list.append(i)

print(f'''Изначальный список: {num_list}
Сдвинутый список: {new_list}''')


