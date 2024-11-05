class Catalog:
    """Class to manage the catalog of e-books."""

    def __init__(self, catalog_id, ebooks, last_updated, total_ebooks, owner):
        # Initialize attributes for the catalog
        self.__catalog_id = catalog_id  # Unique ID for the catalog
        self.__ebooks = ebooks  # List of e-books in the catalog
        self.__last_updated = last_updated  # Date when the catalog was last updated
        self.__total_ebooks = total_ebooks  # Total number of e-books in the catalog
        self.__owner = owner  # owner of the catalog

    # Getter methods to access private attributes
    def get_catalog_id(self):
        # Return the catalog ID
        return self.__catalog_id

    def get_ebooks(self):
        # Return the list of e-books
        return self.__ebooks

    def get_last_updated(self):
        # Return the date when the catalog was last updated
        return self.__last_updated

    def get_total_ebooks(self):
        # Return the total number of e-books in the catalog
        return self.__total_ebooks

    def get_owner(self):
        # Return the owner of the catalog
        return self.__owner

    # Setter methods to change private attributes
    def set_catalog_id(self, catalog_id):
        # Set a new catalog ID
        self.__catalog_id = catalog_id

    def set_ebooks(self, ebooks):
        # Set a new list of e-books
        self.__ebooks = ebooks

    def set_last_updated(self, last_updated):
        # Set a new last updated date
        self.__last_updated = last_updated

    def set_total_ebooks(self, total_ebooks):
        # Set a new total number of e-books
        self.__total_ebooks = total_ebooks

    def set_owner(self, owner):
        # Set a new owner for the catalog
        self.__owner = owner

    # Add an e-book to the catalog
    def add_ebook(self, ebook):
        self.__ebooks.append(ebook)
        self.__total_ebooks += 1
        print("E-book added successfully.")

    # Modify an e-book by title
    def modify_ebook(self, title, new_ebook):
        for ebook in self.__ebooks:
            if ebook.get_title() == title:
                self.__ebooks[self.__ebooks.index(ebook)] = new_ebook
                print("E-book modified successfully.")
                return
        print("E-book not found.")

    # Remove an e-book by title
    def remove_ebook(self, title):
        for ebook in self.__ebooks:
            if ebook.get_title() == title:
                self.__ebooks.remove(ebook)
                self.__total_ebooks -= 1
                print("E-book removed successfully.")
                return
        print("E-book not found.")

    # Method to represent the catalog as a string
    def __str__(self):
        # Return a string showing the catalog ID and the total number of e-books
        return "Catalog ID: " + str(self.__catalog_id) + " | Total E-books: " + str(self.__total_ebooks)
