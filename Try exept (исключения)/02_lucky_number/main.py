import random

with open('out_file.txt', 'w', encoding='UTF-8') as file:
    finish = 0
    while finish < 777:
        try:
            exc = random.randint(1, 13)
            if exc == 13:
                raise BaseException
            num = int(input('Введите число: '))
            file.writelines(str(num) + '\n')
            finish += num
        except BaseException:
            print('Вас постигла неудача!')
            break
    if finish >= 777:
        print('Успех!')

with open('out_file.txt', 'r', encoding='UTF-8') as file:
    print('\nСодержимое файла out_file.txt: ')
    print(file.read())



