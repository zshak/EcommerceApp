from Catalog import Catalog
from Product import Product
import Constants
import os
import csv


# EcommerceApp class
# communicates with Catalog class using only product_id
# prints in console according to output
    
class EcommerceApp:
    def __init__(self):
        self.catalog = Catalog()

    def save_product(self, product_id, product_name, product_price):
        product = Product(product_id, product_name, product_price)
        if self.catalog.add_product(product_id, product_name, product_price) == Constants.ALREADY_IN_CATALOG:
            print(product_id + ": product name updated to " + product_name)
            print(product_id + ": product price updated to " + product_price)
        else:
            print(product_id + " " + product_name + " Successfully added to the catalog")

    def purchase_product(self, product_id, quantity, price):
        if self.catalog.purchase_product(product_id, quantity, price) == Constants.NO_SUCH_PRODUCT:
            print("No such product with the id " + product_id + " in the catalog to purchase")
            return
        print("product " + self.catalog.get_product(product_id).product_name + "(id: " + product_id
              + ") successfully purchased")

    def order_product(self, product_id, quantity):
        status = self.catalog.place_order(product_id, quantity)
        if status == Constants.NO_SUCH_PRODUCT:
            print("No such product in the catalog to order")
            return
        if status == Constants.NOT_ENOUGH_QUANTITY:
            print("Not enough " + self.catalog.get_product(product_id).product_name + "(id: " + product_id
                  + ") left in the stock")
            return
        print("order successfully placed: " + self.catalog.get_product(product_id).product_name
              + "(id: " + product_id + ")")

    def get_quantity_of_product(self, product_id):
        result = self.catalog.get_quantity_of_product(product_id)
        if result == Constants.NO_SUCH_PRODUCT:
            print("No such product with the id " + product_id + " in the catalog")
            return
        print("quantity of the product " + self.catalog.get_product(product_id).product_name
              + "(id: " + product_id + "): " + str(result))

    def get_average_price(self, product_id):
        result = self.catalog.get_product_avg_price(product_id)
        if result == Constants.NO_SUCH_PRODUCT:
            print("No such product with the id " + product_id + " in the catalog")
            return
        print("average price of the product " + self.catalog.get_product(product_id).product_name
              + "(id: " + product_id + "): " + str(result))

    def get_product_profit(self, product_id):
        result = self.catalog.get_product_profit(product_id)
        if result == Constants.NO_SUCH_PRODUCT:
            print("No such product with the id " + product_id + " in the catalog")
            return
        product = self.catalog.get_product(product_id)
        print("profit of the product " + product.product_name
              + "(id: " + product_id + "): " + str(result))

    def get_fewest_product(self):
        result = self.catalog.get_fewest_product()
        if result == Constants.NO_PRODUCTS:
            print("No products in the catalog")
            return
        print("product with the lowest remaining quantity: " + result.product_name
              + "(id: " + result.product_id + ")")

    def get_most_popular_product(self):
        result = self.catalog.get_most_popular_product()
        if result == Constants.NO_PRODUCTS:
            print("No products in the catalog")
            return
        print("product with the highest number of orders: " + result.product_name
              + "(id: " + result.product_id + ")")

    def get_orders_report(self):
        list_of_orders = self.catalog.get_list_of_orders()
        print("Orders report: ")
        for procedure in list_of_orders:
            print(procedure)

    def export_orders_report(self, path):
        list_of_orders = self.catalog.get_list_of_orders()

        path = path.split('\\')
        complete_path_arr = []
        for p in path:
            complete_path_arr += p.split('/')
        complete_path = os.path.join(*complete_path_arr, 'output.csv')
        with open(complete_path, 'w', newline='') as f:
            writer = csv.writer(f)
            for procedure in list_of_orders:
                row = procedure.split()
                writer.writerow(row)
        print('done')