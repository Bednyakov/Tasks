def how_are_you(func):
    def inner():
        _ = input('Как дела? Ответ: ')
        print('А у меня не очень...')
        result = func()
        return result
    return inner

@how_are_you
def test():
    print('Тут что-то происходит...')

test()

