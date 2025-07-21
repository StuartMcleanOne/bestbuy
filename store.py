class Store:
    def __init__(self, products): # Takes list of products
        self.products = products

    def add_product(self, product): # Adds new product to the store
        self.products.append(product)

    def remove_product(self, product): # Removes product
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self): # Aggregates quantity of product
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self): # Filters only active products
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list): # Loops over tuples and buys them, accumulating total cost.
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
