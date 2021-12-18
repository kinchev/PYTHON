from abc import ABC, abstractmethod

import self as self

from Project_1.common.validator import Validator


class Astronaut(ABC):
    @abstractmethod
    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            Validator.raise_if_str_is_empty(value, 'Astronaut name cannot be empty string or whitespace')
        self.__name = value

    def breathe(self):
        self.oxygen -= 10

    def increase_oxygen(self, amount):
        self.oxygen += amount
