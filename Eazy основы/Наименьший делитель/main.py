n = int(input('Введите целое число: '))

def divider(n):
    for i in range(2, n + 1):
        if n % i == 0:
            break
    return i

print(f'Наименьший делитель, отличный от единицы: {divider(n)}')
