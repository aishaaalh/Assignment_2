class Customer:
    """Class to represent a customer in the store."""

    def __init__(self, name, contact_info, loyalty_member, email, address):
        # Initialize attributes for the customer
        self.__name = name  # Name of the customer
        self.__contact_info = contact_info  # Contact information 
        self.__loyalty_member = loyalty_member  # True if the customer is a loyalty member
        self.__email = email  # Customer email address
        self.__address = address  # Customer address

    # Getter methods to access private attributes
    def get_name(self):
        # Return the name of the customer
        return self.__name

    def get_contact_info(self):
        # Return the contact information of the customer
        return self.__contact_info

    def get_loyalty_member(self):
        # Return whether the customer is a loyalty member
        return self.__loyalty_member

    def get_email(self):
        # Return the email address of the customer
        return self.__email

    def get_address(self):
        # Return the address of the customer
        return self.__address

    # Setter methods to change private attributes
    def set_name(self, name):
        # Set a new name for the customer
        self.__name = name

    def set_contact_info(self, contact_info):
        # Set new contact information for the customer
        self.__contact_info = contact_info

    def set_loyalty_member(self, loyalty_member):
        # Set whether the customer is a loyalty member
        self.__loyalty_member = loyalty_member

    def set_email(self, email):
        # Set a new email address for the customer
        self.__email = email

    def set_address(self, address):
        # Set a new address for the customer
        self.__address = address
    
    # Modify customer information
    def modify_customer(self, name=None, contact_info=None, loyalty_member=None, email=None, address=None):
        if name:
            self.__name = name
        if contact_info:
            self.__contact_info = contact_info
        if loyalty_member is not None:
            self.__loyalty_member = loyalty_member
        if email:
            self.__email = email
        if address:
            self.__address = address
        print("Customer information modified successfully.")

    # Method to represent the customer as a string
    def __str__(self):
        # Return a string showing the customer name and email
        return "Customer: " + self.__name + " | Email: " + self.__email
