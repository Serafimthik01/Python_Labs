from . import base
from math import *


class Wallpaper(base.BaseClass):
    # length_Room = 1,
    # width_Room = 1
    # height_Room = 1
    # width_Roll = 1
    # length_Roll = 1
    # quantity = 1
    # cost = 1
    # S_area = 1
    # S_one = 1

    def __init__(self, length_Room, width_Room, height_Room, width_Roll, length_Roll, cost):
        self.length_Room = length_Room
        self.width_Room = width_Room
        self.height_Room = height_Room
        self.width_Roll = width_Roll
        self.length_Roll = length_Roll
        self.cost = cost
        self.calc_S_area()
        self.calc_S_one()
        self.calculation_quantity()

    def calc_S_area(self):
        S_area = 2 * (self.height_Room * self.width_Room) + 2 * (self.height_Room * self.length_Room)
        return S_area

    def calc_S_one(self):
        S_one = self.length_Roll * self.width_Roll
        return S_one

    def calculation_quantity(self):
        self.quantity = self.calc_S_area() / self.calc_S_one()
        return ceil(self.quantity)

    def calc_cost(self):
        cost = self.calculation_quantity() * self.cost
        return cost
