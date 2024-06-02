from abc import ABC, abstractmethod
from .product_dto import ProductDto


class ProductStorage(ABC):
    @abstractmethod
    def save_product(self, product_dto: ProductDto):
        pass

    @abstractmethod
    def _model_to_dto(self, product):
        pass

    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod
    def create_product(self, product_dto: ProductDto):
        pass