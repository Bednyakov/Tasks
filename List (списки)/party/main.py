guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f'\nСейчас на вечеринке {len(guests)} человек: {guests}')
    answer = input('Гость пришел или ушел?')

    if answer != 'Пора спать':
        name = input('Имя гостя: ')
        if len(guests) != 6 and answer == 'пришел':
            guests.append(name)
            print(f'Привет, {name}!')
        elif answer == 'ушел':
            guests.remove(name)
            print(f'Пока, {name}!')
        else:
            print(f'Прости, {name}, но мест нет.')
    else:
        print('Вечеринка закончилась, все легли спать.')
        break

