# -*- coding: utf-8 -*-

import simple_draw as sd
def triangle(start_point, angle, len, color):
    draw(start_point, angle, len, 120, color)


def square(start_point, angle, len, color):
    draw(start_point, angle, len, 90, color)


def pentagon(start_point, angle, len, color):
    draw(start_point, angle, len, 72, color)


def hexagon(start_point, angle, len, color):
    draw(start_point, angle, len, 60, color)


def draw(start_point, angle, len, step, color):
    current_point = start_point
    for i in range(0, 360, step):
        vector = sd.get_vector(current_point, i + angle, len)
        if i == 360 - step:
            sd.line(vector.start_point, start_point, color=color)
        else:
            sd.line(vector.start_point, vector.end_point, color=color)
        current_point = vector.end_point
# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр 02_global_color.py скопировать сюда
# Результат решения см results/exercise_03_shape_select.jpg

# TODO здесь ваш код

shapes = {1: [triangle, 'triangle'], 2: [square, 'square'], 3: [pentagon, 'pentagon'], 4: [hexagon, 'hexagon']}
print("Выберите желаемую фигуру")
for k, v in shapes.items():
    print(k, ':', v[1])
shape = int(input())
while shape > 4 or shape < 1:
    print('incorrect number')
    shape = int(input())
shapes[shape][0](sd.get_point(250, 250), 0, 100, sd.COLOR_ORANGE)
sd.pause()
