data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

# 1
print('Список ключей и значений словаря "data": ')
for keys, values in data.items():
    print(keys, ':', values)

# 2
data['ETH'].update({'total_diff': 100})

# 3
data["tokens"][0]['fst_token_info']['name'] = 'doge'

# 4
count = 0
for i_elem in data["tokens"]:
    for j_elem in i_elem:
        if j_elem == 'total_out':
            data['ETH']['total_out'] += data["tokens"][count][j_elem]
            #del data["tokens"][count][j_elem] этот метод удаления
            #выдает ошибку, пришлось удалять доп циклом
            count += 1
for i in range(len(data["tokens"])):
    data["tokens"][i].pop('total_out')

# 5
data["tokens"][1]['sec_token_info']['total_price'] = data["tokens"][1]['sec_token_info']['price']
del data["tokens"][1]['sec_token_info']['price']





