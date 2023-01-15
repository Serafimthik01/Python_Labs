# -*- coding: utf-8 -*-


class water:
    def __str__(self):
        return 'вода'

    def __add__(self, other):
        if isinstance(other, air):
            return storm()
        elif isinstance(other, fire):
            return vapor()
        elif isinstance(other, earth):
            return dirt()
        else:
            return None


class air:
    def __str__(self):
        return 'воздух'

    def __add__(self, other):
        if isinstance(other, water):
            return storm()
        elif isinstance(other, fire):
            return lightning()
        elif isinstance(other, earth):
            return dust()
        else:
            return None


class fire:
    def __str__(self):
        return 'огонь'

    def __add__(self, other):
        if isinstance(other, water):
            return vapor()
        elif isinstance(other, air):
            return lightning()
        elif isinstance(other, earth):
            return lava()
        else:
            return None


class earth:
    def __str__(self):
        return 'земля'

    def __add__(self, other):
        if isinstance(other, water):
            return dirt()
        elif isinstance(other, air):
            return dust()
        elif isinstance(other, fire):
            return lava()
        elif isinstance(other, earth):
            return earth()
        else:
            return None


class storm:
    def __str__(self):
        return 'шторм'


class vapor:
    def __str__(self):
        return 'пар'


class dirt:
    def __str__(self):
        return 'грязь'


class lightning:
    def __str__(self):
        return 'молния'


class dust:
    def __str__(self):
        return 'пыль'


class lava:
    def __str__(self):
        return 'лава'


print(water(), '+', air(), '=', water() + air())
print(water(), '+', fire(), '=', water() + fire())
print(water(), '+', earth(), '=', water() + earth())
print(air(), '+', fire(), '=', air() + fire())
print(air(), '+', earth(), '=', air() + earth())
print(fire(), '+', earth(), '=', fire() + earth())
print(earth(), '+', fire(), '=', earth() + fire())
print(earth(), '+', earth(), '=', earth() + earth())
