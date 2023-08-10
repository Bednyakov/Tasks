#Задача решается с помощью @lru_cache модуля functools

def number_cache(func):
    """Декоратор кэширует полученные ранее занчения и возвращает их"""
    cache = dict()
    def inner(*args, **kwargs):
        if args in cache:
            return cache[args]
        else:
            value = func(*args, **kwargs)
            cache[args] = value
            return value
    return inner

@number_cache
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


# Вычисление числа Фибоначчи с использованием кеширования
print(fibonacci(10))  # Результат будет кеширован

# Повторное вычисление числа Фибоначчи с теми же аргументами
print(fibonacci(10))  # Результат будет взят из кеша

# Вычисление числа Фибоначчи с другим аргументом
print(fibonacci(5))  # Результат будет вычислен и закеширован
