class Product:
    def __init__(self, name, price, quantity):
        if not name or not isinstance(name, str):
            raise ValueError("Product name must be a non-empty string.")
        if price < 0:
            raise ValueError("Price must be non-negative.")
        if quantity < 0:
            raise ValueError("Quantity must be non-negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        if not self.active:
            raise Exception(f"{self.name} is not active.")
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if quantity > self.quantity:
            raise Exception(f"Not enough stock for {self.name}. Available: {self.quantity}")

        total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return total_price
