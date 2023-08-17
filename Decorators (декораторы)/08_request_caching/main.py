class LRUCache:
    '''Класс хранит запросы и удалять самые старые при достижении лимита'''
    def __init__(self, limit: int = 3):
        self.__limit = limit
        self.__cache = []

    @property
    def cache(self):  # этот метод должен возвращать самый старый элемент
        return self.__cache[0]

    @cache.setter
    def cache(self, new_elem: tuple):  # этот метод должен добавлять новый элемент
        index = 0
        if len(self.__cache) != 0:
            for elem in self.__cache:
                if elem[0] == new_elem[0]:
                    del self.__cache[index]
                    index += 1
        self.__cache.append(new_elem)
        if len(self.__cache) == self.__limit + 1:
            del self.__cache[0]

    def print_cache(self):
        '''Функция выводит содержимое LRU Cache'''
        print('LRU Cache:')
        for elem in self.__cache:
            print(f'{elem[0]} : {elem[1]}')

    def get(self, key: str):
        '''Функция ищет значение по ключу'''
        index = 0
        for elem in self.__cache:
            if key == elem[0]:
                del self.__cache[index]
                self.__cache.append(elem)
                index += 1
                return self.__cache[-1][1]


# Создаем экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.get("key2"))  # value2

# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновленный кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4