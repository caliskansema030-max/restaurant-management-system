from product import Product
from customer import Customer
from order import Order
from restaurant import Restaurant

# Restoran oluştur
restaurant = Restaurant()

# Ürünler oluştur
product1 = Product("Pizza", 250, "Yemek")
product2 = Product("Kola", 70, "İçecek")
product3 = Product("Hamburger", 200, "Yemek")

# Menüye ürün ekle
restaurant.add_product_to_menu(product1)
restaurant.add_product_to_menu(product2)
restaurant.add_product_to_menu(product3)

# ANA PROGRAM
while True:

    print("\n===== RESTORAN YÖNETİM SİSTEMİ =====")
    print("1 - Menüyü Göster")
    print("2 - Sipariş Oluştur")
    print("3 - Siparişleri Göster")
    print("4 - Günlük Ciro")
    print("5 - Çıkış")

    choice = input("Seçiminiz: ")

    # MENÜYÜ GÖSTER
    if choice == "1":

        restaurant.show_menu()

    # SİPARİŞ OLUŞTUR
    elif choice == "2":

        # Müşteri adı kontrolü
        while True:

            customer_name = input("Müşteri adı: ").strip()

            if customer_name == "":
                print("Müşteri adı boş olamaz.")

            else:
                break

        # Masa numarası kontrolü
        while True:

            try:

                table_number = int(input("Masa numarası: "))
                break

            except ValueError:

                print("Lütfen sadece sayı giriniz.")

        # Customer oluştur
        customer = Customer(customer_name, table_number)

        # Order oluştur
        order = Order(customer)

        # Ürün seçme sistemi
        while True:

            print("\n--- ÜRÜNLER ---")

            for i, product in enumerate(restaurant.menu):

                print(f"{i + 1} - {product.name} - {product.price} TL")

            product_choice = input(
                "Ürün seçiniz (Örnek: 1,2 | Bitirmek için q): "
            )

            # Siparişi bitir
            if product_choice.lower() == "q":
                break

            try:

                choices = product_choice.split(",")

                for choice_item in choices:

                    product_index = int(choice_item.strip()) - 1

                    if 0 <= product_index < len(restaurant.menu):

                        selected_product = restaurant.menu[product_index]

                        order.add_product(selected_product)

                        print(selected_product.name, "siparişe eklendi.")

                    else:

                        print("Geçersiz ürün numarası.")

            except ValueError:

                print("Lütfen sadece sayı giriniz.")

        # Siparişi restorana ekle
        restaurant.add_order(order)

        print("Sipariş başarıyla oluşturuldu.")

    # SİPARİŞLERİ GÖSTER
    elif choice == "3":

        restaurant.show_all_orders()

    # GÜNLÜK CİRO
    elif choice == "4":

        income = restaurant.calculate_daily_income()

        print("\nGünlük Toplam Kazanç:", income, "TL")

    # PROGRAMI KAPAT
    elif choice == "5":

        print("Program kapatıldı.")
        break

    else:

        print("Geçersiz seçim yaptınız.")