import datetime

def logging(func):
    """Декоратор выводит имя, документацию функций, и записывает ошибки в файл."""
    def inner():
        try:
            print('Имя функции: ', func.__name__)
            print('Документация: ', func.__doc__)
            result = func()
            return result
        except Exception as exception:
            with open('function_errors.log', 'a', encoding='UTF-8') as logfile:
                logfile.writelines(f'''Дата/время: {datetime.datetime.now()}
Функция: "{func.__name__}"
Ошибка: "{exception}"
\n''')

    return inner

@logging
def test1():
    """Документация"""
    print('Функция выполнена.')

@logging
def test2():
    #Документация
    print(Zzzzzzzzzzzz)

@logging
def test3():
    print('Функция выполнена.')

@logging
def test4():
    """Документация"""
    print(Zzzzz)

test1()
test2()
test3()
test4()