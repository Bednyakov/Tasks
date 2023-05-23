site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}

def find_key(data, my_key, depth):
    if depth > 0:
        if my_key in data:
            return data[my_key]
    for element in data.values():
        if isinstance(element, dict):
            result = find_key(element, my_key, depth - 1)
            if result:
                break
    else:
        result = None
    return result

user_key = input('Введите искомый ключ: ')
depth = input('Использовать глубину: (Y/N): ').lower()
if depth == 'y':
	depth = int(input('Введите глубину поиска: '))
else:
	depth = 15

print(f'Значение ключа: ', find_key(site, user_key, depth))






