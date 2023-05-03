films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
user_films = []

amt = int(input('Сколько фильмов хотите добавить?'))

for _ in range(amt):
    film = input('Введите название фильма: ')
    if film in films:
        user_films.append(film)
    else:
        print(f'Ошибка. Фильма "{film}" у нас нет :(')

print('Ваш список любимых фильмов: ', end='')
print(*user_films, sep=', ')

