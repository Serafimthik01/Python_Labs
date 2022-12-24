#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

sd.resolution = (1200, 600)
y2 = 0
number = 0
for y1 in range(0, 600, 50):
    y2 += 50
    number += 1
    if number % 2 == 0:
        x2 = 0
        range_x1 = range(0, 1200, 100)
    else:
        x2 = 50
        range_x1 = range(-50, 1100, 100)
    for x1 in range_x1:
        x2 += 100
        sd.rectangle(left_bottom=sd.get_point(x1, y1), right_top=sd.get_point(x2, y2), color=sd.COLOR_ORANGE, width=1)
sd.pause()
