class Store:
    """Class to represent the e-book store."""

    def __init__(self, store_name, location, contact_number, catalog, open_status):
        # Initialize attributes for the store
        self.__store_name = store_name  # Name of the store
        self.__location = location  # Location of the store
        self.__contact_number = contact_number  # Contact number for the store
        self.__catalog = catalog  # Catalog of e-books available in the store
        self.__open_status = open_status  # True if the store is open False if closed

    # Getter methods to access private attributes
    def get_store_name(self):
        # Return the store name
        return self.__store_name

    def get_location(self):
        # Return the location of the store
        return self.__location

    def get_contact_number(self):
        # Return the contact number of the store
        return self.__contact_number

    def get_catalog(self):
        # Return the catalog of e-books
        return self.__catalog

    def get_open_status(self):
        # Return whether the store is open or not
        return self.__open_status

    # Setter methods to change private attributes
    def set_store_name(self, store_name):
        # Set a new store name
        self.__store_name = store_name

    def set_location(self, location):
        # Set a new location for the store
        self.__location = location

    def set_contact_number(self, contact_number):
        # Set a new contact number for the store
        self.__contact_number = contact_number

    def set_catalog(self, catalog):
        # Set a new catalog for the store
        self.__catalog = catalog

    def set_open_status(self, open_status):
        # Set a new open/closed status for the store
        self.__open_status = open_status
    
    # Modify store information
    def modify_store(self, store_name=None, location=None, contact_number=None, open_status=None):
        if store_name:
            self.__store_name = store_name
        if location:
            self.__location = location
        if contact_number:
            self.__contact_number = contact_number
        if open_status is not None:
            self.__open_status = open_status
        print("Store information modified successfully.")

    # Method to represent the store as a string
    def __str__(self):
        # Return a string showing the store name and location
        return "Store Name: " + self.__store_name + " | Location: " + self.__location
