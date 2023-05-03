h_string = input('Введите строку: ')
h_count = 0
count = 0
for i in h_string:
    if i == 'h':
        h_count += 1
        if h_count == 1:
            start = count
        else:
            stop = count
    count += 1

print(f'Развёрнутая последовательность между первым и последним h: {h_string[stop-1:start:-1]}')
