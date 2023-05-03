message = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
abc_string = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
new_message = ''

for i in message:
    if i == ' ':
        new_message += i
    for j in abc_string:
        if i == j:
            if (abc_string.index(j) + shift) < len(abc_string):
                new_message += abc_string[abc_string.index(j) + shift]
            else:
                indx = len(abc_string) - (abc_string.index(j) + shift)
                new_message += abc_string[indx]

print(new_message)
