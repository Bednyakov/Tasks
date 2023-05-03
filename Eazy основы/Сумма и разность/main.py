num = input('Введите целое число: ')

def sum_num(num):
    sumnum = 0
    for i in num:
        sumnum += int(i)
    return sumnum

def amt(num):
    count = 0
    for i in num:
        count += 1
    return count

print(f'''Сумма чисел: {sum_num(num)}
Количество цифр в числе: {amt(num)}
Разность суммы и количества цифр: {int(sum_num(num)) - int(amt(num))}''')


