from sale.domain.product.exceptions import ProductNameIsInvalid


class Product(object):
    id: int
    name: str

    def __init__(self, name):
        self.id = None
        self.name = name

    def is_valid(self):
        if self.name is None or self.name == "":
            raise ProductNameIsInvalid("Product name is invalid")

        return True

    def create_product(self):
        self.is_valid()
