from abc import ABC, abstractmethod
from .sale_dto import SaleDto


class SaleStorage(ABC):

    @abstractmethod
    def save_sale(self, sale_dto: SaleDto):
        pass

    @abstractmethod
    def _model_to_dto(self, sale):
        pass

    @abstractmethod
    def get_all_sales(self):
        pass
