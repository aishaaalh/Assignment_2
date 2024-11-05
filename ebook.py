class Ebook:
    """Class to represent an e-book in the store."""

    def __init__(self, title, author, publication_date, genre, price):
        # Initialize attributes for the e-book
        self.__title = title  # Title of the e-book
        self.__author = author  # Author of the e-book
        self.__publication_date = publication_date  # Date when the e-book was published
        self.__genre = genre  # Genre of the e-book
        self.__price = price  # Price of the e-book

    # Getter methods to access private attributes
    def get_title(self):
        # Return the title of the e-book
        return self.__title

    def get_author(self):
        # Return the author of the e-book
        return self.__author

    def get_publication_date(self):
        # Return the publication date of the e-book
        return self.__publication_date

    def get_genre(self):
        # Return the genre of the e-book
        return self.__genre

    def get_price(self):
        # Return the price of the e-book
        return self.__price

    # Setter methods to change private attributes
    def set_title(self, title):
        # Set a new title for the e-book
        self.__title = title

    def set_author(self, author):
        # Set a new author for the e-book
        self.__author = author

    def set_publication_date(self, publication_date):
        # Set a new publication date for the e-book
        self.__publication_date = publication_date

    def set_genre(self, genre):
        # Set a new genre for the e-book
        self.__genre = genre

    def set_price(self, price):
        # Set a new price for the e-book
        self.__price = price

    # Method to represent the e-book as a string
    def __str__(self):
        # Return a string showing the title and author of the e-book
        return "Ebook: " + self.__title + " by " + self.__author
