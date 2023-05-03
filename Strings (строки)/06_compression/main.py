user_string = input('Введите строку: ')
temp = ''
broken = ''
new_string = ''

for i in user_string:
    if i != temp:
        broken += ' ' + i
        temp = i
    else:
        broken += i

for i in broken.split():
    new_string += str(i[0]) + str(len(i))

print('Закодированная строка: ', new_string)
