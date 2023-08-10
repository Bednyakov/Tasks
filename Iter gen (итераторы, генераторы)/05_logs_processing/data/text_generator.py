import random
import datetime

# Изменяя N можно управлять количеством строк в файле
N = 100_000_000


error_names = ['ValueError', 'ArithmeticError', 'AssertionError', 'ImportError', 'NameError', 'OSError']

with open('work_logs.txt', 'w', encoding='utf8') as file:
    for _ in range(N):
        if random.randint(1, 10) == 5:
            text = 'ERROR: ' + random.choice(error_names) + ' ' + str(datetime.datetime.today())
        else:
            text = 'COMPLETE: Данные успешно переданы.'
        file.write(text + '\n')
