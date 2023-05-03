user_str = input('Введите текст: ')
let = 'аеёиоуыэюя'
let_list = [x for x in user_str if x in let]

print(f'Список гласных букв: {let_list}')
print(f'Длина списка: {len(let_list)}')
