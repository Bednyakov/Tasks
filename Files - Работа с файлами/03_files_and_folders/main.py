import os

user_path = input('Введите путь: ')

def path_scan(abs_path, folders = 0, files = 0):
    for i in os.listdir(abs_path):
        path = os.path.join(abs_path, i)
        if os.path.isfile(path): files += 1
        if os.path.isdir(path): folders += 1
    size = os.path.getsize(abs_path)
    return size, folders, files

print(f'Размер каталога, количество подкаталогов и файлов: {path_scan(user_path)}')


