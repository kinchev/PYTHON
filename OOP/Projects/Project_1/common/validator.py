from abc import ABC, abstractmethod


class Validator:
    @staticmethod
    def raise_if_str_is_empty(self, value, error_message):
        if value.strip() == '':
            raise ValueError(error_message)
