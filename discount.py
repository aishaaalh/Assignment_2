class Discount:
    """Class to manage discounts in the store."""

    def __init__(self, discount_id, description, percentage, conditions, is_active):
        # Initialize attributes for the discount
        self.__discount_id = discount_id  # Unique ID for the discount
        self.__description = description  # Description of the discount
        self.__percentage = percentage  # Discount percentage
        self.__conditions = conditions  # Conditions for applying the discount
        self.__is_active = is_active  # True if the discount is currently active

    # Getter methods to access private attributes
    def get_discount_id(self):
        # Return the discount ID
        return self.__discount_id

    def get_description(self):
        # Return the description of the discount
        return self.__description

    def get_percentage(self):
        # Return the discount percentage
        return self.__percentage

    def get_conditions(self):
        # Return the conditions for the discount
        return self.__conditions

    def get_is_active(self):
        # Return whether the discount is active
        return self.__is_active

    # Setter methods to change private attributes
    def set_discount_id(self, discount_id):
        # Set a new discount ID
        self.__discount_id = discount_id

    def set_description(self, description):
        # Set a new description for the discount
        self.__description = description

    def set_percentage(self, percentage):
        # Set a new discount percentage
        self.__percentage = percentage

    def set_conditions(self, conditions):
        # Set new conditions for the discount
        self.__conditions = conditions

    def set_is_active(self, is_active):
        # Set whether the discount is active or not
        self.__is_active = is_active
    
    # Method to calculate and apply discount
    def apply_discount(self, total_price, num_ebooks, is_loyalty_member):
        if not self.__is_active:
            return total_price  # No discount if not active
        
        # Loyalty program 10% discount
        if is_loyalty_member and "loyalty" in self.__conditions:
            total_price *= 0.9
        
        # Bulk purchase 20% discount 5 or more e-books
        if num_ebooks >= 5 and "bulk" in self.__conditions:
            total_price *= 0.8
        
        return total_price

    # Modify discount details
    def modify_discount(self, description=None, percentage=None, conditions=None, is_active=None):
        if description:
            self.__description = description
        if percentage is not None:
            self.__percentage = percentage
        if conditions:
            self.__conditions = conditions
        if is_active is not None:
            self.__is_active = is_active
        print("Discount modified successfully.")

    # Method to represent the discount as a string
    def __str__(self):
        # Return a string showing the description and percentage of the discount
        return "Discount: " + self.__description + " | Percentage: " + str(self.__percentage) + "%"
