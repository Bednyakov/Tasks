user_ip = input('Введите IP: ')
ip_string = ''.join(user_ip.split('.'))

if ip_string.isdigit() == True:
    ip_list = [int(x) for x in user_ip.split('.')]
    if max(ip_list) > 255:
        print(f'{max(ip_list)} превышает 255.')

    elif user_ip.count('.') != 3 and len(ip_list) != 4:
        print('Адрес — это четыре числа, разделённые точками.')

    else:
        print('IP-адрес корректен')
else:
    print('Строка состоит не из целых чисел.')



