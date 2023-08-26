
def decorator_with_args_for_any_decorator(func):
  """ Декоратор для приема аргументов другим декоратором"""
  def inner(*args, **kwargs):
    print(f'Переданные арги и кварги в декоратор: {args}, {kwargs}')
    result = func(*args, **kwargs)
    return result
  return inner


@decorator_with_args_for_any_decorator
def decorated_decorator(func, *args, **kwargs):
    """Декоратор. Шаблон"""
    def decorator(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
        return inner
    return decorator


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)

decorated_function("Юзер", 101)
