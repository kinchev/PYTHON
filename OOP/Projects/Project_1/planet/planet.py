from Project_1.common.validator import Validator


class Planet:
    def __init__(self, name):
        self.name = name
        items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            Validator.raise_if_str_is_empty(value, 'Planet name cannot be empty string or whitespace!')
        self.__name = value
