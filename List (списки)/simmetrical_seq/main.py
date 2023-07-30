nums = int(input('Введите количество чисел: '))
num_list = []
first_list = []
second_list = []

for i in range(nums):
    num = int(input(f'Число {i + 1}: '))
    num_list.append(num)
first_list.extend(num_list)

for j in range(len(num_list)):
    half = len(num_list) // 2
    if len(num_list) % 2 != 0:
        if num_list[:half] == num_list[half + 1:]:
            break
    else:
        if num_list[:half] == num_list[:half-1:-1]:
            break
    num_list.append(num_list[j])
    second_list.append(num_list[j])

print(f'''\nПоследовательность: {first_list}
Нужно приписать чисел: {len(second_list)}
Сами числа: {second_list}''')
