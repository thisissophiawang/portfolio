"""
XINYI WANG
CS 5001, Fall 2023
Unitest for Product class
"""
#ls
#python3 -m unittest tests.test_product

from unittest import TestCase
from unittest.mock import patch
from models.product import Product
import requests

class TestProduct(TestCase):
    def test_product_fetch(self):
        product = Product()
        with patch('models.product.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = [
                {
                    "id": 1,
                    "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
                    "price": 109.95,
                    "description": "Your perfect pack for everyday use...",
                    "category": "men's clothing",
                    "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",
                    "rating": {"rate": 3.9, "count": 120}
                },
            ]
            product.fetch_products()
            self.assertIsNotNone(product.products)
            self.assertEqual(len(product.products), 1)
            self.assertEqual(product.products[0]['title'], 'Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops')
            self.assertEqual(product.products[0]['price'], 109.95)


    # writing the serve down test
    def test_product_fetch_with_connection_error(self):
        product = Product()
        with patch('models.product.requests.get') as mock_get:
            mock_get.side_effect = requests.exceptions.ConnectionError
            product.fetch_products()
            self.assertEqual(len(product.product), 0)    


    # writing the “non-200 status code” test
    def test_product_fetch_with_status_code_not_200(self):
        product = Product()
        with patch('models.product.requests.get') as mock_get:
            mock_get.return_value.status_code = 500
            product.fetch_products()
            self.assertEqual(len(product.product), 0)


    # writing the “bad status message” test
    def test_product_fetch_bad_status(self):
        product = Product()
        with patch('models.product.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            product.fetch_products()
            self.assertEqual(len(product.product), 0)


