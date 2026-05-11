class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def show_info(self):
        print("Ürün Adı:", self.name)
        print("Fiyat:", self.price)
        print("Kategori:", self.category)