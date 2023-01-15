# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

sd.resolution = (900, 800)


class Snowflake:
    # TODO здесь ваш код
    def __init__(self):
        self.point = sd.get_point(sd.random_number(0, 900), sd.random_number(890, 2000))
        self.length = sd.random_number(25, 60)
        self.f_a = sd.random_number(1, 8) / 10
        self.f_b = sd.random_number(1, 7) / 10
        self.f_c = sd.random_number(35, 65)

    def clear_previous_picture(self):
        sd.snowflake(center=self.point, length=self.length, color=sd.background_color,
                     factor_a=self.f_a, factor_b=self.f_b, factor_c=self.f_c)

    def move(self):
        self.point.x += sd.random_number(-10, 10)
        self.point.y -= sd.random_number(5, 15)

    def draw(self):
        sd.snowflake(center=self.point, length=self.length, color=sd.COLOR_WHITE,
                     factor_a=self.f_a, factor_b=self.f_b, factor_c=self.f_c)

    def can_fall(self):
        if self.point.y > 15:
            return True
        else:
            return False


flake = Snowflake()

# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


N = 20


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

def get_flakes(count):
    return [Snowflake() for _ in range(count)]


flakes = get_flakes(count=N)


def get_fallen_flakes():
    global flakes
    res = 0
    for flake in flakes:
        if not flake.can_fall():
            res += 1
            flakes.remove(flake)
    return res


def append_flakes(count):
    global flakes
    for _ in range(count):
        flake = Snowflake()
        flakes.append(flake)


while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
