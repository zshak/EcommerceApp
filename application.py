from EcommerceApp import EcommerceApp

if __name__ == '__main__':
    app = EcommerceApp()
    command_to_function = {
        'save_product': app.save_product,
        'purchase_product' : app.purchase_product,
        'order_product' : app.order_product,
        'get_quantity_of_product' : app.get_quantity_of_product,
        'get_average_price': app.get_average_price,
        'get_product_profit': app.get_product_profit,
        'get_fewest_product': app.get_fewest_product,
        'get_most_popular_product': app.get_most_popular_product,
        'get_orders_report': app.get_orders_report,
        'export_orders_report': app.export_orders_report
    }
    while True:
        command = input('Enter command: ').strip().split()
        if len(command) == 0:
            continue
        command_name = command[0]
        if command_name == 'exit':
            break
        if command_name not in command_to_function:
            print("illegal command")
            continue
        args = command[1:]
        
        try:
            command_to_function[command_name](*args)
        except:
            print("illegal number of arguments")