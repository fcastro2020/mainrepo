class MyAdditionOperation:
    def __init__(self, factor: str):
        self.factor = factor

    def add_numbers(self, a: int = 0, b: int = 0):
        c = (a + b) * self.factor
        return c
