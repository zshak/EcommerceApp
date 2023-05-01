import Constants
from Product import Product

class Catalog:
    # initializes Catalog class
    # product_id -> product
    # we need to keep track of the products in the catalog
    # and identify each product id with product object
    def __init__(self):
        self.products = {}


    # type: boolean
    # returns true if the product is present in the catalog
    # false otherwise
    def contains_product(self, product_id):
        return product_id in self.products


    # type: product
    # returns product if present in the catalog
    # else returns None
    def get_product(self, product_id):
        if self.contains_product(product_id):
            return self.products[product_id]
        return None


    def get_quantity_of_product(self, product_id):
        if self.contains_product(product_id):
            return self.get_product(product_id).quantity
        return Constants.NO_SUCH_PRODUCT


    # type: int
    # return ALREADY_IN_CATALOG if product was already in the catalog
    # updates product and returns SUCCESSFULLY_PROCCESSED
    def add_product(self, product_id, product_name, product_price):
        if self.contains_product(product_id):
            product_to_update = self.get_product(product_id)
            product_to_update.product_name = product_name
            product_to_update.product_price = product_price
            return Constants.ALREADY_IN_CATALOG

        self.products[product_id] = Product(product_id, product_name, product_price)
        return Constants.SUCCESSFULLY_PROCCESSED


    # type: int
    # returns NO_SUCH_PRODUCT if the product is not pressent in the catalog
    # else purchases amount = quantity products for the given price and returns SUCCESSFULLY_PROCCESSED
    def purchase_product(self, product_id, quantity, price):
        if not self.contains_product(product_id):
            return Constants.NO_SUCH_PRODUCT
        product = self.get_product(product_id)
        product.add_entry(quantity, price)
        return Constants.SUCCESSFULLY_PROCCESSED


    # type: int
    # returns SUCCESSFULLY_PROCCESSED if order has been successfully placed
    # returns NOT_ENOUGH_QUANTITY if not enough products are lef
    # returns NO_SUCH_PRODUCT if the product is not pressent in the catalog
    def place_order(self, product_id, quantity):
        if not self.contains_product(product_id):
            return Constants.NO_SUCH_PRODUCT

        product = self.products[product_id]
        if product.quantity < int(quantity):
            return Constants.NOT_ENOUGH_QUANTITY

        product.sell(quantity)
        return Constants.SUCCESSFULLY_PROCCESSED


    # type: int
    # returns NO_SUCH_PRODUCT if the product is not pressent in the catalog
    # else returns product average price
    def get_product_avg_price(self, product_id):
        if not self.contains_product(product_id):
            return Constants.NO_SUCH_PRODUCT
        product = self.get_product(product_id)
        return product.get_average_price()


    # type: int
    # returns returns NO_SUCH_PRODUCT if the product is not pressent in the catalog
    # else returns product profit
    def get_product_profit(self, product_id):
        if not self.contains_product(product_id):
            return Constants.NO_SUCH_PRODUCT
        product = self.get_product(product_id)
        return product.get_product_profit()


    # type: int/product
    # returns NO_PRODUCTS if there are no products in the catalog
    # else returns the product with the least quantity left
    def get_fewest_product(self):
        if len(self.products) == 0:
            return Constants.NO_PRODUCTS
        products = self.products.values()
        fewest_product = min(products, key=lambda k: k.quantity)
        return fewest_product


    # type: int/product
    # returns NO_PRODUCTS if there are no products in the catalog
    # else returns the product with the most quantity left
    def get_most_popular_product(self):
        if len(self.products) == 0:
            return Constants.NO_PRODUCTS
        products = self.products.values()
        popular_product = max(products, key=lambda k: sum(order.quantity for order in k.order_history))
        return popular_product


    def get_list_of_orders(self):
        list_of_orders = []
        for product in self.products.values():
            list_of_orders += product.get_list_of_product_orders()
        return list_of_orders