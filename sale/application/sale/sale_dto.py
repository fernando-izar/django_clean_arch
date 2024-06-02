from datetime import datetime
from sale.domain.sale.entities import Sale
from sale.application.product.product_dto import ProductDto


class SaleDto(object):
    date: datetime
    product_dto: ProductDto

    def __init__(self, date: datetime, product_dto: ProductDto, quantity):
        self.id = None
        self.date = date
        self.product_dto = product_dto
        self.quantity = quantity

    def _to_domain(self):
        return Sale(
            date=self.date,
            product=self.product_dto._to_domain(),
            quantity=self.quantity,
        )
