from sale.domain.sale.exceptions import SaleDateIsInvalid, SaleQuantityIsInvalid
from sale.application.sale.sale_dto import SaleDto
from sale.domain.product.exceptions import ProductNameIsInvalid
from sale.application.sale.sale_storage import SaleStorage


class SaleManager(object):
    storage: SaleStorage

    def __init__(self, storage: SaleStorage) -> None:
        self.storage = storage

    def create_new_sale(self, sale_dto: SaleDto):
        sale_domain_obj = sale_dto._to_domain()

        try:
            if sale_domain_obj.is_valid():
                return "save"
        except SaleDateIsInvalid as e:
            return {"message": e.message}
        except SaleQuantityIsInvalid as e:
            return {"message": e.message}
        except ProductNameIsInvalid as e:
            return {"message": e.message}

    def get_sales(self):
        return self.storage.get_all_sales()
