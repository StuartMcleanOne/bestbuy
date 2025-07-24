"""
Product module for store inventory management.

Defines the Product class used to represent an individual item for sale.
"""

class Product:
    """
    Represents a product available in the store.

    Attributes:
        name (str): The name of the product.
        price (float): The price of a single unit.
        quantity (int): Number of units in stock.
        active (bool): Product availability status.
    """

    def __init__(self, name, price, quantity):
        """
        Initialize a new Product instance.

        Args:
            name (str): Name of the product.
            price (float): Price of the product.
            quantity (int): Initial quantity in stock.

        Raises:
            ValueError: If name is empty or price/quantity are negative.
        """
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
        """
        Returns the current quantity of the product.

        Returns:
            int: Quantity in stock.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Updates the product's quantity.

        Args:
            quantity (int): New quantity to set.

        Raises:
            ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """
        Checks if the product is active.

        Returns:
            bool: True if active, False otherwise.
        """
        return self.active

    def activate(self):
        """Sets product status to active."""
        self.active = True

    def deactivate(self):
        """Sets product status to inactive."""
        self.active = False

    def show(self):
        """Prints a formatted string representing the product."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        """
        Processes purchase of the product.

        Args:
            quantity (int): Quantity to purchase.

        Returns:
            float: Total cost of the purchase.

        Raises:
            Exception: If product is inactive or out of stock.
            ValueError: If quantity is invalid.
        """
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
