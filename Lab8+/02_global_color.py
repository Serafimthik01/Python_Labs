# -*- coding: utf-8 -*-
import simple_draw as sd


def triangle(start_point, angle, len, color):
    draw(start_point, angle, len, 120, color)


def square(start_point, angle, len, color):
    draw(start_point, angle, len, 90, color)


def five(start_point, angle, len, color):
    draw(start_point, angle, len, 72, color)


def six(start_point, angle, len, color):
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


# Добавить цвет в функции рисования геом. фигур. из упр 01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см /results/exercise_02_global_color.jpg
colors = {1: [sd.COLOR_RED, 'red'], 2: [sd.COLOR_ORANGE, 'orange'], 3: [sd.COLOR_DARK_YELLOW, 'yellow'],
          4: [sd.COLOR_GREEN, 'green'], 5: [sd.COLOR_CYAN, 'cyan'], 6: [sd.COLOR_BLUE, 'blue'],
          7: [sd.COLOR_PURPLE, 'purple']}
print('выберите желаемый цвет')
for k, v in colors.items():
    print(k, ':', v[1])
color = int(input())
while color > 7 or color < 1:
    print("incorrect number")
    color = int(input())
triangle(sd.get_point(100, 100), 0, 100, colors[color][0])
square(sd.get_point(300, 100), 0, 100, colors[color][0])
five(sd.get_point(100, 300), 0, 100, colors[color][0])
six(sd.get_point(400, 300), 0, 100, colors[color][0])
# TODO здесь ваш код

sd.pause()
