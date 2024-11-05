class Cart:
    """Class to manage the shopping cart."""

    def __init__(self, customer, items, total_price, discount_applied, order_date):
        # Initialize attributes for the cart
        self.__customer = customer  # The customer who has the cart
        self.__items = items  # List of items in the cart
        self.__total_price = total_price  # Total price of the items in the cart
        self.__discount_applied = discount_applied  # Any discount applied to the cart
        self.__order_date = order_date  # Date when the order was created

    # Getter methods to access private attributes
    def get_customer(self):
        # Return the customer name
        return self.__customer

    def get_items(self):
        # Return the list of items
        return self.__items

    def get_total_price(self):
        # Return the total price of items
        return self.__total_price

    def get_discount_applied(self):
        # Return whether a discount was applied
        return self.__discount_applied

    def get_order_date(self):
        # Return the order date
        return self.__order_date

    # Setter methods to change private attributes
    def set_customer(self, customer):
        # Set a new customer name
        self.__customer = customer

    def set_items(self, items):
        # Set a new list of items
        self.__items = items

    def set_total_price(self, total_price):
        # Set a new total price for the cart
        self.__total_price = total_price

    def set_discount_applied(self, discount_applied):
        # Set if a discount is applied or not
        self.__discount_applied = discount_applied

    def set_order_date(self, order_date):
        # Set a new order date
        self.__order_date = order_date
    
     # Method to apply discounts based on conditions
    def calculate_total_with_discounts(self, discount, is_loyalty_member):
        num_ebooks = len(self.__items)
        self.__total_price = discount.apply_discount(self.__total_price, num_ebooks, is_loyalty_member)
        return self.__total_price
    
    # Add an item to the cart
    def add_item(self, item):
        self.__items.append(item)
        self.__total_price += item.get_price()  # Assuming each item has a get_price method
        print("Item added to the cart.")

    # Modify an item in the cart by title
    def modify_item(self, old_item_title, new_item):
        for item in self.__items:
            if item.get_title() == old_item_title:
                self.__total_price -= item.get_price()  # Remove old item price
                self.__items[self.__items.index(item)] = new_item
                self.__total_price += new_item.get_price()  # Add new item price
                print("Item modified in the cart.")
                return
        print("Item not found in the cart.")

    # Remove an item from the cart by title
    def remove_item(self, item_title):
        for item in self.__items:
            if item.get_title() == item_title:
                self.__total_price -= item.get_price()  # Subtract item price from total
                self.__items.remove(item)
                print("Item removed from the cart.")
                return
        print("Item not found in the cart.")

    # Method to represent the cart as a string
    def __str__(self):
        # Return a string showing the customer and the number of items
        return "Cart for " + str(self.__customer) + " | Total Items: " + str(len(self.__items))
