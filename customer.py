from enum import Enum


class Gender(Enum):
    Male = 0
    Female = 1


class Customer:

    def __init__(self, name, id, balance, gender):
        self.name = name
        self.id = id
        self.balance = balance
        self.gender = gender






