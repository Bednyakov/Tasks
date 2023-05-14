phone_book = dict()

while True:
    print('''Введите номер действия:
    1. Добавить контакт
    2. Найти человека
    0. Выйти''')
    user_act = int(input())
    if user_act == 1:
        name = tuple(input('Введите имя контакта: ').split())
        tel = input('Введите номер телефона: ')
        phone_book[name] = tel
        print(f'Текущий словарь: {phone_book}')
    if user_act == 2:
        search = input('Введите имя: ')
        for i in phone_book:
            for j in i:
                if search.lower() == j.lower():
                    print(*i, phone_book[i])
    if user_act == 0:
        break



