class Order:
    """Class to handle orders in the store."""

    def __init__(self, order_id, cart, order_status, payment_status, delivery_status):
        # Initialize attributes for the order
        self.__order_id = order_id  # Unique ID for the order
        self.__cart = cart  # The cart associated with the order
        self.__order_status = order_status  # Current status of the order
        self.__payment_status = payment_status  # Status of payment 
        self.__delivery_status = delivery_status  # Status of delivery 

    # Getter methods to access private attributes
    def get_order_id(self):
        # Return the order ID
        return self.__order_id

    def get_cart(self):
        # Return the cart linked to the order
        return self.__cart

    def get_order_status(self):
        # Return the current status of the order
        return self.__order_status

    def get_payment_status(self):
        # Return the status of payment for the order
        return self.__payment_status

    def get_delivery_status(self):
        # Return the delivery status of the order
        return self.__delivery_status

    # Setter methods to change private attributes
    def set_order_id(self, order_id):
        # Set a new order ID
        self.__order_id = order_id

    def set_cart(self, cart):
        # Set a new cart for the order
        self.__cart = cart

    def set_order_status(self, order_status):
        # Set a new status for the order
        self.__order_status = order_status

    def set_payment_status(self, payment_status):
        # Set a new payment status
        self.__payment_status = payment_status

    def set_delivery_status(self, delivery_status):
        # Set a new delivery status
        self.__delivery_status = delivery_status

    # Method to calculate final price with discounts applied
    def calculate_final_price(self, discount, is_loyalty_member):
        return self.__cart.calculate_total_with_discounts(discount, is_loyalty_member)

     # Modify order details
    def modify_order(self, order_status=None, payment_status=None, delivery_status=None):
        if order_status:
            self.__order_status = order_status
        if payment_status:
            self.__payment_status = payment_status
        if delivery_status:
            self.__delivery_status = delivery_status
        print("Order modified successfully.")
        
    # Method to represent the order as a string
    def __str__(self):
        # Return a string showing the order ID and current status
        return "Order ID: " + str(self.__order_id) + " | Status: " + self.__order_status
