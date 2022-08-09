from enum import Enum


class Type(Enum):
    Regular = 0
    Israeli = 1


class Product:

    def __init__(self, company, name, bar_code, price, type):
        self.company = company
        self.name = name
        self.bar_code = bar_code
        self.price = price
        self.type = type

