num_orders = int(input('Введите количество заказов: '))
orders_dict = {}
for i in range(1, num_orders + 1):
    new_string = input(f'{i} заказ: ')
    new_list = new_string.split()

    if new_list[0] not in orders_dict:
        orders_dict[new_list[0]] = {new_list[1]: int(new_list[2])}
    else:
        if new_list[1] not in orders_dict[new_list[0]]:
            orders_dict[new_list[0]][new_list[1]] = int(new_list[2])
        else:
            orders_dict[new_list[0]][new_list[1]] |= int(new_list[2])


for i in sorted(orders_dict):
    print(f'\n{i}:')
    for k, v in sorted(orders_dict[i].items()):
        print(f"\t{k}: {v}")

