

class MyMath:

    @classmethod
    def circumference(cls, radius: int) -> float:
        '''Функция вычисляет длину окружности через диаметр'''
        result = (2 * 3.14 * radius)
        return result

    @classmethod
    def areacircle(cls, radius: int) -> float:
        '''Функция вычисляет площадь круга через радиус'''
        result = (3.14 * (radius ** 2))
        return result

    @classmethod
    def cubevolume(cls, edge: int) -> float:
        '''Функция вычисляет объем куба'''
        result = (edge ** 3)
        return result

    @classmethod
    def splherearea(cls, radius: int) -> float:
        '''Функция вычисляет площадь поверхности сферы'''
        result = (4 * 3.14 * (radius ** 2))
        return result


res_1 = MyMath.circumference(5)
res_2 = MyMath.areacircle(6)
print(res_1, res_2)

# Предупреждение на случай запуска модуля как программы
if __name__ == "__main__":
    raise Exception('Был запущен импортируемый модуль!')
