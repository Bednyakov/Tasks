import time

class LoggerDecorator:
    '''Класс-декоратор логирующий аргуметы
    и время выполнения функций.'''

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time() - start
        print(f'Вызывается функция {self.func.__name__}')
        print(f'Аргументы {args, kwargs}')
        print(f'Результат: {result}')
        print(f'Время выполнения: {end} секунд.')
        return self.func(*args, **kwargs)
