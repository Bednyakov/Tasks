def singleton(cls):
  """Декоратор- определитель инициализации экземпляра класса."""
  def inner():
    if cls.__copy is None:
      cls.__copy = cls()
    return cls.__copy
  cls.__copy = None
  return inner


