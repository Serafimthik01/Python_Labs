#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances1 = ((550 - 510) ** 2 + (370 - 510) ** 2) ** 0.5
distances2 = ((550 - 480) ** 2 + (370 - 480) ** 2) ** 0.5
distances3 = ((510 - 480) ** 2 + (510 - 480) ** 2) ** 0.5

# TODO здесь заполнение словаря

print("Moscow-London =", round(distances1))
print("Moscow-Paris  =", round(distances2))
print("London-Paris  =", round(distances3))




