class Product:
    """Represents a product in the store."""

    def __init__(self, name, price, category, stock=0):
        """Initializes the product."""
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock


class ShoppingCart:
    """Represents a customer's shopping cart."""

    def __init__(self):
        """Initializes the shopping cart."""
        self.items = {}

    def add_item(self, product, quantity=1):
        """Adds a product to the cart."""
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove_item(self, product):
        """Removes a product from the cart."""
        if product in self.items:
            del self.items[product]

    def update_quantity(self, product, quantity):
        """Updates the quantity of a product in the cart."""
        if product in self.items:
            if quantity > 0:
                self.items[product] = quantity
            else:
                self.remove_item(product)


class Customer:
    """Represents a customer."""

    def __init__(self, name):
        """Initializes the customer."""
        self.name = name
        self.order_history = []


class Order:
    """Represents an order made by a customer."""

    def __init__(self, customer, cart, discount=0.1, tax_rate=0.05):
        """Initializes the order and processes the purchase."""
        self.customer = customer
        self.items = cart.items
        self.total_price = self._calculate_total(discount, tax_rate)
        customer.order_history.append(self)

    def _calculate_total(self, discount, tax_rate):
        """Calculates the final price including discounts and taxes."""
        subtotal = sum(
            product.price * quantity for product, quantity in self.items.items()
        )
        after_discount = subtotal * (1 - discount)
        return after_discount * (1 + tax_rate)
