players = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']

print('Первый день: ', players[::2])

# более сложный вариант:
set_players = []
count = 0
for i in players:
    if count % 2 == 0:
        set_players.append(i)
    count += 1
print('\nВариант второй: ')
print(f'Первый день: {set_players}')

