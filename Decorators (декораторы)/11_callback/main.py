
app = {}

def callback(route: str):
  """Функция обратного вызова"""

  def decorator(func):
    app[route] = func

    def inner(*args, **kwargs):
      result = func(*args, **kwargs)
      return result(*args, **kwargs)
    return inner
  return decorator


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')



