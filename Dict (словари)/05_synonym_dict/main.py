syn_dict = {}
num = int(input('Введите количество пар слов: '))

for i in range(1, num + 1):
    new_string = input(f'{i}-я пара (разделите дефисом с пробелами): ')
    new_list = new_string.split(' - ')
    new_element = {new_list[0]: new_list[1]}
    syn_dict.update(new_element)

synonim = ' '
temp = ''
while synonim != '':
    synonim = input('\nВведите слово (Enter для выхода): ')
    for k, v in syn_dict.items():
        if k.lower() == synonim.lower():
            temp = syn_dict[k]
        if v.lower() == synonim.lower():
            temp = k
    if temp != '':
        print(f'Синоним: {temp}')
    else:
        print('Такого слова в словаре нет.')
    temp = ''
