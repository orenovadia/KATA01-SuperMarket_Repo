# ----------------------------------------------- #
# Intro to Kata 01:                               #
# Super_Market management & pricing kata Project. #
# ----------------------------------------------- #
# Background
# ==========
# Writing a program witch operates
# the supermarket.
#
# Project Description
# ====================
# In this super market we have entities witch are mainly objects:
# The super market's objects are:
#
# Inventory Managment - handle the stock:
#   1) the inventory is a list or a dictionary of products (the key) and how many in stock (value).
#   2) add and remove products or a few units from its stock from the warehouse.
#   3) prints the full stock.
#
# A Product - entity:
#   Every Product contains the fields:
#     1) Barcode.
#     2) Category.
#     3) Name.
#     4) Full Price.
#     5) Units of measuring.
#
# A Shopping Cart - entity:
#   Every Cart Is:
#     1) A list or a dictionary of products (the key) and how many of each one in the cart (value).
#     2) add and remove products or a few units from the cart.
#
# -----------------------------------------------------------------------------


import unittest

from supermarket.super_market import Inventory
from supermarket.super_market import Product
from supermarket.super_market import Cart

# because Cart and Inventory are so much alike, You had to copy their code, which is almost completely identical 
# accept for naming. But here you also had to duplicate the tests for it.
# I suggest this Design for both of them:

class ProductCollection(object):
    def __init__(self):
        self.products = {}
    def add_product(self, product, amount):
        pass 
        # ...


class ShoppingCart(ProductCollection):
    pass


class Inventory(ProductCollection):
    pass

# Then, You only need to test product collection
# Another alternative is to not even define the class Cart, but rather instantiate ProductCollection:
# cart = ProductCollection()
# inventory = ProductCollection()
# This would work as long as both cart and inventory don't have their own seperate logic. Then you need to subclass
# Product collection for both of them and extend it. For example:

class ShoppingCart(ProductCollection):
    def calculate_price(self):
        return sum(p.full_price * amount for p, amount in self.products.iteritems())

class TestShoppingCart(unittest.TestCase):

    def test_add_product(self):
        my_product = Product(73459, 'Milk & Eggs', 'yammy eggs', 12.50, 'small packs')
        my_cart = Cart()
        my_cart.add_product(my_product, 20)

        self.assertIn(my_product, my_cart.products)
        assert len(my_cart.products) == 1
        assert my_cart.products[my_product] == 20

    def test_remove_product(self):
        my_product = Product(73459, 'Milk & Eggs', 'yammy eggs', 12.50, 'small packs')
        my_cart = Cart()
        my_cart.add_product(my_product, 20)

        my_cart.remove_product(my_product, 5)
        assert my_cart.products[my_product] == 15

        my_cart.remove_product(my_product, 16)
        assert my_cart.products[my_product] == 0


class TestInventory(unittest.TestCase):

    def test_add_to_stock(self):
        my_product = Product(73459, 'Milk & Eggs', 'yammy eggs', 12.50, 'small packs')
        my_inv = Inventory()
        my_inv.add_to_stock(my_product, 20)

        self.assertIn(my_product, my_inv.stock)
        assert len(my_inv.stock) == 1
        assert my_inv.stock[my_product] == 20

    def test_remove_from_stock(self):
        my_product = Product(73459, 'Milk & Eggs', 'yammy eggs', 12.50, 'small packs')
        my_inv = Inventory()
        my_inv.add_to_stock(my_product, 20)

        my_inv.remove_from_stock(my_product, 5)
        assert my_inv.stock[my_product] == 15

        my_inv.remove_from_stock(my_product, 16)
        assert my_inv.stock[my_product] == 0


if __name__ == '__main__':
    unittest.main()
