num = int(input('Введите число: '))
set_num = []

for i in range(num + 1):
    if i % 2 != 0:
        set_num.append(i)

print(f'Список нечетных чисел от 1 до {num}: {set_num}')
