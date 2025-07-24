"""
Store module for managing product inventory and purchases.

Defines the Store class, which holds multiple Product instances and
allows for adding/removing products, checking quantities, and processing orders.
"""

class Store:
    """
    Represents a store containing a list of available products.

    Attributes:
        products (List[Product]): A list of products stocked in the store.
    """

    def __init__(self, products):
        """
        Initializes a new Store instance.

        Args:
            products (List[Product]): Initial list of product objects.
        """
        self.products = products

    def add_product(self, product):
        """
        Adds a new product to the store.

        Args:
            product (Product): The product to add.
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        Removes a product from the store if it exists.

        Args:
            product (Product): The product to remove.
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        """
        Returns the total quantity of all products in the store.

        Returns:
            int: Total quantity in stock.
        """
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        """
        Retrieves all products that are currently active.

        Returns:
            List[Product]: A list of active products.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        """
        Processes an order composed of multiple products and quantities.

        Args:
            shopping_list (List[Tuple[Product, int]]): List of (product, quantity) pairs.

        Returns:
            float: Total price of the order.

        Raises:
            Exception: If a product cannot be purchased.
        """
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
