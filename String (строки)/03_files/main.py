while True:
    file_name = input('Название файла: ')
    badsym = '@№$%^&\*('

    if not file_name.endswith(('.txt', '.docx')):
        print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
    elif file_name.startswith(tuple(badsym)):
        print('Ошибка: название начинается на один из специальных символов.')
    else:
        print('Файл назван верно.')
        break


