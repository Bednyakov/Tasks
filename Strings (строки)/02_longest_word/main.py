text = input('Введите текст: ').split()
word = max(text, key=len)

print(f'''Самое длинное слово: {word}
Длина этого слова: {len(word)}''')
