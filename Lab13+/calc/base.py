from abc import ABC, abstractmethod


class BaseClass(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calc_S_area(self):
        pass

    @abstractmethod
    def calc_S_one(self):
        pass

    @abstractmethod
    def calculation_quantity(self):
        pass

    @abstractmethod
    def calc_cost(self):
        pass
