from sale.application.sale.sale_storage import SaleStorage
from sale.application.sale.sale_dto import SaleDto

class SaleRepositoryTest(SaleStorage):
        def _model_to_dto(self, sale):
            return SaleDto(
                 date = sale.date,
                 product_dto = sale.product_dto,
                 quantity = sale.quantity
            )

        def get_all_sales(self):
            pass
        def save_sale(self, sale_dto: SaleDto):
            return "save"