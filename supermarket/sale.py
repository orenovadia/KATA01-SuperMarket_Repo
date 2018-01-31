from abc import ABCMeta, abstractmethod

'''
And a comment abuot the design of the sales here. 
What does the method payment return? I dont understand, the price of the cart? the price of the products that the sale works on? or the price reduced by the sale?

If you return the price of the products that the sale applies to, If two sales run on the same product will you pay for it twice?
'''

# Sale interface
class Sale(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def payment(self, cart):
        # calculate the cart's default price.
        # this is an abstract method, Abstract is the opposite of concrete. 
        # it is not supposed to be called or do anything, 
        # And another thing, Why should a "Sale" calculate the price of a cart. 
        # A cart could do it, or a different object
        cart_price = 0

        for p, amount in cart.products.iteritems():
            prod_price = p.full_price * amount
            cart_price += prod_price

        return cart_price


class XPercent(Sale):
    def __init__(self, product, percent):
        self.percent_price = product.full_price * percent

    def payment(self, cart):
        # What if the product is not in the cart at all?
        # Then you don't get any of this discount.
        return self.percent_price


class OnePlusOne(Sale):
    def __init__(self, buy_this, get_that):
        self.buy_this = buy_this
        self.get_that = get_that

    def payment(self, cart):
        # n_buys = cart.products[self.buy_this]
        # The above may raise a KeyError if the product is not in the cart
        n_buys = cart.products.get(self.buy_this, 0)
        n_gets= cart.products.get(self.get_that, 0)
       
        buy_full_price = self.buy_this.full_price
        get_full_price = self.get_that.full_price

        # if you get the same product.
        if self.buy_this is self.get_that:  # when comparing objects "is" is more clear than equality
            # instead of checking the remainder of modulu 2, can simly round the number down
            return n_buys // 2 * buy_full_price

        # if you get other product
        # if self.buy_this != self.get_that:
        # why write the exact opposite condition rather than use "else"?
        else:
            # if n_buys > n_gets:
            #    cart.products[self.get_that] = n_buys # HEY HEY HEY, what are you doing here? you are changing the contents of the cart. Did you mean to do that?

            #here, you probably want to calculate the times that the sale applies
            n = min(n_buys, n_gets)
            # ....
            # and another thing about this method. I think it wwould be easier to calculate the full price of these two producs in the beginning and after substract the amount of the sale before you return it.
