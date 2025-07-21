from products import Product

def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))         # Expected: 12500
    print(mac.buy(100))         # Expected: 145000
    print(mac.is_active())      # Expected: False

    bose.show()                 # Should reflect quantity 450
    mac.show()                  # Quantity 0, inactive

    bose.set_quantity(1000)
    bose.show()                 # Quantity should now be 1000

if __name__ == "__main__":
    main()
