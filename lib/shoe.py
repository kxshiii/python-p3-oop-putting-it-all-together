#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def __str__(self):
        return f'{self.brand} shoe, size {self.size}'

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"