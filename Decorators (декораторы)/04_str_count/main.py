def counter(func):
    """Декоратор считает количество вызовов функции"""

    def inner():
        inner.count += 1
        result = func()
        return result

    inner.count = 0
    return inner

@counter
def test1():
    pass

@counter
def test2():
    pass


test1()
test1()
test2()
test2()
test2()

print(test1.count)
print(test2.count)