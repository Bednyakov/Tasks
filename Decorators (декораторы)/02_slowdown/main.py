import time

def time_delay(func):
    """Декоратор создает задержку времени запуска функции."""
    def inner(seconds: int = 3):
        for _ in range(seconds * 3):
            print('▓▓', end='')
            time.sleep(0.33)
        print('100%\n')
        result = func()
        return result
    return inner

@time_delay
def testfunc():
    print('Функция запущена!')

testfunc()

