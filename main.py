"""Best Buy Store CLI
This module provides a command-line interface for interacting with the store.
Users can view available products, check store inventory, place orders, or exit.
"""

from products import Product
from store import Store

def start(store):
    """
    Launches the interactive menu for the store.

    Args:
        store (Store): The store instance containing available products.
    """
    while True:
        print("\n--- Welcome to Best Buy ---")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            print("\n--- Products Available ---")
            for product in store.get_all_products():
                product.show()

        elif choice == "2":
            total = store.get_total_quantity()
            print(f"\nTotal quantity in store: {total}")

        elif choice == "3":
            print("\n--- Place an Order ---")
            order_items = []
            products = store.get_all_products()

            for index, product in enumerate(products, start=1):
                print(f"{index}. {product.name} (Price: {product.price}, Available: {product.quantity})")

            while True:
                try:
                    selection = input("Enter product number to order (or press Enter to finish): ").strip()
                    if not selection:
                        break
                    product_index = int(selection) - 1
                    if product_index not in range(len(products)):
                        print("Invalid product number.")
                        continue
                    quantity = int(input(f"Enter quantity for {products[product_index].name}: "))
                    order_items.append((products[product_index], quantity))
                except ValueError:
                    print("Invalid input. Please enter numeric values.")

            try:
                total_price = store.order(order_items)
                print(f"\nOrder placed! Total price: ${total_price}")
            except Exception as e:
                print(f"Order failed: {e}")

        elif choice == "4":
            print("Thank you for shopping at Best Buy! 👋")
            break

        else:
            print("Invalid choice. Please select a valid option.")

def main():
    """
    Initializes the product inventory and starts the CLI interface.
    """
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = Store(product_list)
    start(best_buy)

if __name__ == "__main__":
    main