class SaleDateIsInvalid(Exception):
    def __init__(self, message):
        self.message = message

class SaleQuantityIsInvalid(Exception):
    def __init__(self, message):
        self.message = message