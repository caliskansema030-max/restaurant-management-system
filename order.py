class Order:
    def __init__(self, customer):
        self.customer = customer
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        total = 0

        for product in self.products:
            total += product.price

        return total

    def show_order(self):
        print("Müşteri:", self.customer.name)
        print("Masa No:", self.customer.table_number)

        print("\nSiparişler:")

        for product in self.products:
            print("-", product.name, "-", product.price, "TL")

        print("\nToplam Tutar:", self.calculate_total(), "TL")