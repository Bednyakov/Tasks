from datetime import datetime
import time


def logged(cls, func, fmt_str):
  """Декоратор для логирования вызываемого метода класса."""

  def inner(*args, **kwargs):
    print(f'Запускается "{cls.__name__}.{func.__name__}". '
          f'Дата и время запуска: {datetime.now().strftime(fmt_str)}')
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time() - start
    print(f'Завершение "{cls.__name__}.{func.__name__}", '
          f'время работы = {round(end, 3)}s')
    return result
  return inner

def log_methods(fmt_str: str):
  """Декоратор для логирования класса."""
  def decorator(cls):
    for i_method in dir(cls):
      if i_method.startswith('__'):
        continue
      value = getattr(cls, i_method)
      if hasattr(value, '__call__'):
        decorated_a = logged(cls, value, fmt_str)
        setattr(cls, i_method, decorated_a)
    return cls
  return decorator


