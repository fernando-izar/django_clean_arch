from datetime import datetime
from sale.domain.product.entities import Product
from sale.domain.sale.exceptions import SaleDateIsInvalid, SaleQuantityIsInvalid


class Sale(object):
    date: datetime
    product: Product

    def __init__(self, date: datetime, product: Product, quantity):
        self.id = None
        self.date = date
        self.product = product
        self.quantity = quantity

    def is_valid(self):
        if self.date is None:
            raise SaleDateIsInvalid("Sale date is invalid")
        if self.quantity is None or self.quantity <= 0:
            raise SaleQuantityIsInvalid("Sale quantity is invalid")

        try:
            if self.product.is_valid():
                pass
        except Exception as e:
            return {"message": e.message}

        return True
