class Restaurant:

    def __init__(self):
        self.menu = []
        self.orders = []

    def add_product_to_menu(self, product):
        self.menu.append(product)

    def show_menu(self):

        print("\n--- MENÜ ---")

        for product in self.menu:
            print(product.name, "-", product.price, "TL")

    def add_order(self, order):
        self.orders.append(order)

    def show_all_orders(self):

        print("\n--- TÜM SİPARİŞLER ---")

        for order in self.orders:

            order.show_order()

            print("-------------------")

    def calculate_daily_income(self):

        total_income = 0

        for order in self.orders:

            total_income += order.calculate_total()

        return total_income