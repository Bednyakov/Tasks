def plndrm(user_string):

    str_2 = ''
    str_3 = ''

    for i in user_string:
        if i not in str_2:
            str_2 += i
            if user_string.count(i) % 2 == 0:
                str_3 += i

    if len(set(user_string) - set(str_3)) < 2:
        print('Можно сделать палиндромом.')
    else:
        print('Нельзя сделать палиндромом.')

user_string = input('Введите строку: ')
plndrm(user_string)


