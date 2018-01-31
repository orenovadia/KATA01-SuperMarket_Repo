import unittest
from supermarket.super_market import Product, Cart
from supermarket.sale import XPercent, OnePlusOne


class TestXPercentOff(unittest.TestCase):

    def test_payment(self):
        product1 = Product(73459, 'Milk & Eggs', 'yammy eggs', 12.50, 'small packs')
        product2 = Product(43568, 'Meet & Chicken', 'shnitzel', 43.50, 'kg')
        product3 = Product(76768, 'Drinks & Alkohol', 'wain', 55.50, 'bottles')

        cart = Cart()
        # Why do you need all the products in here? 1 is enough no? 2 tops
        cart.add_product(product1, 2)
        cart.add_product(product2, 3)
        cart.add_product(product3, 6)

        pay_product = XPercent(product1, 0.5)

        self.assertEqual(pay_product.payment(cart), 6.25)


class TestOnePlusOne(unittest.TestCase):

    def test_payment(self):
        product1 = Product(73459, 'Milk & Eggs', 'yammy eggs', 12.50, 'small packs')
        product2 = Product(43568, 'Meet & Chicken', 'shnitzel', 43.50, 'kg')
        product3 = Product(76768, 'Drinks & Alkohol', 'wain', 55.50, 'bottles')

        cart = Cart()
        cart.add_product(product1, 2)
        cart.add_product(product2, 1)
        cart.add_product(product3, 6)

        pay_for_products = OnePlusOne(product1, product3)
        pay_for_products2 = OnePlusOne(product1, product2)
        # You didn't test the following:
        # buy 1 get 1 fot the same product
        # One of the products or two of the products are not in the cart at all, and about that, you need to decide whether it is legal for someone to do it, and then you return 0, or the price of the products or whatever, or it is illegal, then you raise an error

        self.assertEqual(pay_for_products.payment(cart), 247)
        self.assertEqual(pay_for_products2.payment(cart), 25.0)
        self.assertEqual(cart.products[product1], 2)
        self.assertEqual(cart.products[product2], 2)


if __name__ == '__main__':
    unittest.main() 
