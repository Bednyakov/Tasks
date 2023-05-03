import random

sq1_list = [round(random.uniform(5.00, 10.00), 2) for _ in range(20)]
sq2_list = [round(random.uniform(5.00, 10.00), 2) for _ in range(20)]
winners_list = [sq1_list[i] if sq1_list[i] > sq2_list[i] else sq2_list[i]
                for i in range(20)]

print(f'''Первая команда: {sq1_list}
Вторая команда: {sq2_list}
Победители тура: {winners_list}''')
