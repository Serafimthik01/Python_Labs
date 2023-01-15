from . import base
from math import *


class Laminat(base.BaseClass):
    # length_Area = 0
    # width_Area = 0
    # width_One = 0
    # length_One = 0
    # quantity = 0
    # cost = 0
    # S_area = 0
    # S_one = 0

    def __init__(self, length_Area, width_Area, square_One, cost):
        self.length_Area = length_Area
        self.width_Area = width_Area
        self.square_One = square_One
        self.cost = cost
        self.calc_S_area()
        self.calc_S_one()
        self.calculation_quantity()

    def calc_S_area(self):
        S_area = self.length_Area * self.width_Area
        return S_area

    def calc_S_one(self):
        return super().calc_S_one()

    def calculation_quantity(self):
        self.quantity = self.calc_S_area() / self.square_One
        return ceil(self.quantity)

    def calc_cost(self):
        cost = self.calculation_quantity() * self.cost
        return cost
