from . import base
from math import *


class Tile(base.BaseClass):
    # length_Area = 0
    # width_Area = 0
    # width_One = 0
    # length_One = 0
    # quantity = 0
    # cost = 0
    # S_area = 0
    # S_one = 0

    def __init__(self, length_Area, width_Area, width_One, length_One, cost):
        self.length_Area = length_Area
        self.width_Area = width_Area
        self.width_One = width_One
        self.length_One = length_One
        self.cost = cost
        self.calc_S_area()
        self.calc_S_one()
        self.calculation_quantity()

    def calc_S_area(self):
        S_area = self.length_Area * self.width_Area
        return S_area

    def calc_S_one(self):
        S_one = (self.length_One / 100) * (self.width_One / 100)
        return S_one

    def calculation_quantity(self):
        self.quantity = self.calc_S_area() / self.calc_S_one()
        return ceil(self.quantity)

    def calc_cost(self):
        cost = self.calculation_quantity() * self.cost
        return cost
