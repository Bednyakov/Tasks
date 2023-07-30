frst_list = list(input('Первая строка: '))
scnd_list = list(input('Вторая строка: '))

count = 0
for _ in range(len(frst_list)):
    if scnd_list == frst_list:
        print(f'Первая строка получается из второй со сдвигом {count}.')
        break
    else:
        scnd_list.insert(0, scnd_list[-1])
        scnd_list.pop()
        count += 1

if scnd_list != frst_list:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
