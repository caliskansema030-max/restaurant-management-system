class Customer:
    def __init__(self, name, table_number):
        self.name = name
        self.table_number = table_number

    def show_customer(self):
        print("Müşteri Adı:", self.name)
        print("Masa Numarası:", self.table_number)