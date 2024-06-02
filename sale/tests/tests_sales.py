import unittest
from datetime import datetime
import sys
import os

# Adicione o diretório raiz do projeto ao PYTHONPATH
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
root_dir = os.path.dirname(parent_dir)
sys.path.append(root_dir)

# sys.path.append("..")
# sys.path.append("../..")
from sale.domain.sale.entities import Sale
from sale.application.sale.sale_dto import SaleDto
from sale.domain.sale.exceptions import SaleDateIsInvalid
from sale.domain.product.entities import Product
from sale.application.product.product_dto import ProductDto
from sale.application.sale.sale_manager import SaleManager
from sale.application.sale.sale_storage import SaleStorage
from sale.tests.repository_test import SaleRepositoryTest


class SaleTests(unittest.TestCase):

    def test_sale_date_is_invalid(self):
        sale = Sale(date=None, product=None, quantity=1)

        with self.assertRaises(SaleDateIsInvalid) as ex:
            sale.is_valid()

        exception = ex.exception

        self.assertEqual(exception.message, "Sale date is invalid")

    def test_sale_quantity_is_invalid(self):
        sale = Sale(date=datetime.now(), product=None, quantity=0)

        with self.assertRaises(Exception) as ex:
            sale.is_valid()

        exception = ex.exception

        self.assertEqual(exception.message, "Sale quantity is invalid")

    def test_sale_create(self):
        date = datetime.now()
        product_dto = ProductDto(name="Product 1")
        quantity = 1
        sale_dto = SaleDto(
            date=date,
            product_dto=product_dto,
            quantity=quantity,
        )
        repository = SaleRepositoryTest()
        manager = SaleManager(repository)
        res = manager.create_new_sale(sale_dto)
        self.assertEqual(res, "save")


if __name__ == "__main__":
    unittest.main()