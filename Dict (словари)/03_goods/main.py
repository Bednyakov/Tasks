goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for i in goods:
    code = goods[i]
    sum_prise = 0
    sum_quant = 0
    if code in store:
        for j in range(len(store[code])):
            sum_prise += store[code][j]['quantity'] * store[code][j]['price']
            sum_quant += store[code][j]['quantity']
    print(f'{i} - {sum_quant} штук, стоимость {sum_prise} руб.')

