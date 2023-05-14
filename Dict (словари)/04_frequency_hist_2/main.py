def inversdict(text, freq_dict):
    invert_dict = {}

    for key in freq_dict.values():
        if key not in invert_dict:
            tempdict = {key: []}
            invert_dict.update(tempdict)

    for symb in text:
        if symb in freq_dict:
            values = freq_dict[symb]
            if symb not in invert_dict[values]:
                invert_dict[values] += symb

    print(f'\nИнвертированный словарь:')
    for k, v in sorted(invert_dict.items()):
        print(k, ': ', v)



text = input('Введите текст: ').lower()
freq_dict = dict()
for symb in text:
    if symb not in freq_dict:
        freq_dict[symb] = 1
    else:
        freq_dict[symb] += 1

print('Оригинальный словарь частот: ')
for k, v in sorted(freq_dict.items()):
    print(k, ':', v)



inversdict(text, freq_dict)






