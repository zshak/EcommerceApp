class Order:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = int(quantity)
        self.price = int(price)

    def to_string(self):
        product = self.product
        res = product.product_id + " " + product.product_name + " " + str(self.quantity) + " " + str(self.price)
        return res