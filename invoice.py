class Invoice:
    """Class to generate and manage invoices."""

    def __init__(self, invoice_id, order, total_before_tax, total_after_tax, vat_rate):
        # Initialize attributes for the invoice
        self.__invoice_id = invoice_id  # Unique ID for the invoice
        self.__order = order  # The order associated with the invoice
        self.__total_before_tax = total_before_tax  # Total amount before applying tax
        self.__total_after_tax = total_after_tax  # Total amount after applying tax
        self.__vat_rate = vat_rate  # VAT applied to the total

    # Getter methods to access private attributes
    def get_invoice_id(self):
        # Return the invoice ID
        return self.__invoice_id

    def get_order(self):
        # Return the order linked to the invoice
        return self.__order

    def get_total_before_tax(self):
        # Return the total amount before tax
        return self.__total_before_tax

    def get_total_after_tax(self):
        # Return the total amount after tax
        return self.__total_after_tax

    def get_vat_rate(self):
        # Return the VAT rate
        return self.__vat_rate

    # Setter methods to change private attributes
    def set_invoice_id(self, invoice_id):
        # Set a new invoice ID
        self.__invoice_id = invoice_id

    def set_order(self, order):
        # Set a new order for the invoice
        self.__order = order

    def set_total_before_tax(self, total_before_tax):
        # Set a new total amount before tax
        self.__total_before_tax = total_before_tax

    def set_total_after_tax(self, total_after_tax):
        # Set a new total amount after tax
        self.__total_after_tax = total_after_tax

    def set_vat_rate(self, vat_rate):
        # Set a new VAT rate
        self.__vat_rate = vat_rate

     # Method to calculate total with VAT after discount
    def calculate_total_with_vat(self, discount, is_loyalty_member):
        total_after_discount = self.__order.calculate_final_price(discount, is_loyalty_member)
        self.__total_after_tax = total_after_discount * (1 + self.__vat_rate / 100)
        return self.__total_after_tax

    # Modify invoice details
    def modify_invoice(self, total_before_tax=None, total_after_tax=None, vat_rate=None):
        if total_before_tax is not None:
            self.__total_before_tax = total_before_tax
        if total_after_tax is not None:
            self.__total_after_tax = total_after_tax
        if vat_rate is not None:
            self.__vat_rate = vat_rate
        print("Invoice modified successfully.")

    # Method to represent the invoice as a string
    def __str__(self):
        # Return a string showing the invoice ID and total amount after tax
        return "Invoice ID: " + str(self.__invoice_id) + " | Total after tax: $" + str(self.__total_after_tax)
