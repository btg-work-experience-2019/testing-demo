'''
Exposes a class and three functions that perform an amazing calculation
based on user inputs.
'''

def add_two_then_square(value):
    return 2 + value * value

def plus_ten(value):
    return value + 10

def subtract_one(value):
    return value - 1


class FormulaRunner:

    def __init(self, input):
        self.input
        self.output = 0

    def run(self):
        self.output = plus_ten(self.value)
        self.output = subtract_one(self.output)
        return add_two_then_square(self.output)
