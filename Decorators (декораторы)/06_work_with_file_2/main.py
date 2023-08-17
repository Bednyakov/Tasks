class File:
    '''Класс контекст-менеджера File'''

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode, encoding='UTF-8')
        except FileNotFoundError:
            print(f'Создан файл {self.filename}')
            self.file = open(self.filename, 'w', encoding='UTF-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type is FileNotFoundError or FileExistsError:
            return True

with File('doc.txt', 'r') as file:
    newfile = file.read()
