amt = int(input('Количество видеокарт: '))
set_card = []

count = 1
for _ in range(amt):
    card = int(input(f'{count} Видеокарта: '))
    set_card.append(card)
    count += 1

max_card = set_card[0] # но проще использовать функцию max()
for i in set_card:
    if i > max_card:
        max_card = i

new_set_card = []
for i in set_card:
    if i != max_card:
        new_set_card.append(i)

print(f'''\nСтарый список видеокарт: {set_card}
Новый список видеокарт: {new_set_card}''')



