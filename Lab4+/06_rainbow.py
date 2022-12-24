#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (500, 500)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
x = 50
x1 = 350

for i in range(len(rainbow_colors)):
    x += 5
    x1 += 5
    sd.line(sd.Point(x, 50), sd.Point(x1, 450), color=rainbow_colors[i], width=4)
# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
sd.clear_screen()
point = sd.get_point(250, 0)
radius = 200
color = sd.COLOR_RED
for i in range(len(rainbow_colors)):
    radius -= 5
    sd.circle(center_position=point, radius=radius, color=rainbow_colors[i], width=4)

sd.pause()

