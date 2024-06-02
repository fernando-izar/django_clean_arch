from sale.application.product.product_dto import ProductDto
from sale.application.product.product_manager import ProductManager
from sale.application.product.product_storage import ProductStorage


class ProductManager:
    storage: ProductStorage

    def __init__(self, storage: ProductStorage) -> None:
        self.storage = storage

    def get_products(self):
        return self.storage.get_all_products()

    def create_product(self, product_dto: ProductDto):
        product = product_dto._to_domain()

        try:
            product.create_product()
            final_dto = product_dto._to_dto(product)
            self.storage.create_product(final_dto)
            return {"message": "Product created successfully", "code": 201}
        except Exception as e:
            return {"message": str(e), "code": 400}