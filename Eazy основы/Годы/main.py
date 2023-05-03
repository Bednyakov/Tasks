year_a = int(input('Введите первый год: '))
year_b = int(input('Введите второй год: '))
print(f'Годы от {year_a} до {year_b} с тремя одинаковыми цифрами: ')

def years(a,b):
    for year in range(a, b + 1):
        for i in str(year):
            if str(year).count(i) == 3:
                print(year)
                break

years(year_a, year_b)




