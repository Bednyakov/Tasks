
def ranking():
    num_cont = int(input('Введите количество контейнеров: '))
    set_weight = []

    for _ in range(num_cont):
        cont_weight = int(input('Введите вес контейнера: '))
        if cont_weight <= 200:
            set_weight.append(cont_weight)
        else:
            print('Перегруз. Давайте заново.')
            ranking()

    new_cont = int(input('Введите вес нового контейнера: '))
    if new_cont > 200:
        print('Перегруз. Давайте заново.')
        ranking()

    count = 0
    for i in set_weight:
        count += 1
        if i >= new_cont:
            continue
        else:
            break

    print(f'Номер, который получит новый контейнер: {count}')

ranking()


