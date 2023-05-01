from Order import Order
class Product:
    def __init__(self, product_id, product_name, product_price, quantity=0):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = int(product_price)
        self.purchase_history = []
        self.order_history = []
        self.quantity = quantity


    # adds purchase
    def add_entry(self, quantity, price):
        self.quantity += int(quantity)
        self.purchase_history.append((int(price), int(quantity)))
        return


    # type: int
    # returns average price based on purchase history
    def get_average_price(self):
        if len(self.purchase_history) == 0:
            return 0
        money_spent_history = [price * quantity for price, quantity in self.purchase_history]
        quantity_bought_history = [quantity for price, quantity in self.purchase_history]
        total_money_spent = sum(money_spent_history)
        total_quantity_bought = sum(quantity_bought_history)
        return total_money_spent / total_quantity_bought


    # type: int
    # returns product profit based on order hirstory
    def get_product_profit(self):
        if len(self.purchase_history) == 0:
            return 0
        avg_purchase_price = self.get_average_price()

        avg_order_price = self.__get_selling_price_and_quantity()
        profit_per_unit = avg_order_price[0] - avg_purchase_price
        return profit_per_unit * avg_order_price[1]


    # places an order of given quantity for product
    def sell(self, quantity):
        self.quantity -= int(quantity)
        order = Order(self, quantity, self.product_price)
        self.order_history.append(order)


    def get_list_of_product_orders(self):
        res = []
        for order in self.order_history:
            res.append(order.to_string())
        res.append("COGS: " + str(self.get_average_price()))
        res.append("selling price: " + str(self.__get_selling_price_and_quantity()[0]))
        return res


    def __get_selling_price_and_quantity(self):
        if len(self.order_history) == 0:
            return (0, 0)
        money_gained_history = [order.price * order.quantity for order in self.order_history]
        quantity_sold_history = [order.quantity for order in self.order_history]
        total_money_gained = sum(money_gained_history)
        total_products_sold = sum(quantity_sold_history)
        selling_price = total_money_gained / total_products_sold
        return (selling_price, total_products_sold)