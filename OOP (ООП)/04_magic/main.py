class Water:
    title = '*>Вода<*'
    def __add__(self, other):
        if isinstance(other, Ground):
            return Dirt()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Air):
            return Storm()
        else:
            return None

class Ground:
    title = '-=Земля=-'
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None

class Fire:
    title = '\Огонь/'
    def __add__(self, other):
        if isinstance(other, Ground):
            return Lava()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        else:
            return None

class Air:
    title = '~Воздух~'
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Ground):
            return Dust()
        elif isinstance(other, Water):
            return Storm()
        else:
            return None

class Dirt:
    title = '|Грязь|'

class Storm:
    title = '>>>Шторм<<<'

class Steam:
    title = '}Пар{'

class Lightning:
    title = 'z-Молния-z'

class Dust:
    title = '.:Пыль:.'

class Lava:
    title = '^Лава^'

fire = Fire()
air = Air()
magic = air + fire

print(f'''Смешиваем {fire.title} и {air.title}:
И получаем {magic.title}.''')
