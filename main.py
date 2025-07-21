from products import Product
from store import Store

from products import Product
from store import Store

def main():
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)

    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())                     # Expected: 850
    print(best_buy.order([(products[0], 1), (products[1], 2)]))  # Expected: 1450 + 500 = 1950

if __name__ == "__main__":
    main()
