
class Date:

    def __init__(self):
        self.__date = Date.from_string

    @classmethod
    def from_string(cls, value: str) -> str:
        '''Метод класса Date конвертирующий полученную строку в дату'''
        if cls.is_date_valid(value):
            newvalue = tuple(value.split('-'))
            result = f'День: {newvalue[0]}   Месяц: {newvalue[1]}   Год: {newvalue[2]}'
            return result

    @classmethod
    def is_date_valid(cls, value: str) -> bool:
        '''Метод класса Date проверяющий валидность даты'''
        result = value.split('-')
        if len(result) == 3 and \
                32 > int(result[0]) > 0 \
                and 13 > int(result[1]) > 0:
            return True
        else:
            return False

    def get_date(self):
        return self.__date

    def __str__(self):
        return self.get_date



date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))


