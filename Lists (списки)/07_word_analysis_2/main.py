word = input('Введите слово: ')
count = len(word) // 2

if len(word) % 2 == 0:
    if word[:count] != word[:count -1:-1]:
        print('Слово не является палиндромом.')
    else:
        print('Слово палиндром.')
else:
    if word[:count] != word[:count:-1]:
        print('Слово не является палиндромом.')
    else:
        print('Слово палиндром.')

