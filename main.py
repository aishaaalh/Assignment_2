# main.py

from ebook import Ebook
from customer import Customer
from cart import Cart
from order import Order
from discount import Discount
from invoice import Invoice
from catalog import Catalog
from store import Store

# Create a catalog with a few e-books
ebook1 = Ebook("Desert Tales", "Maitha Al Qasimi", "2023-06-10", "Adventure", 12.99)
ebook2 = Ebook("Leadership in Modern Times", "Zayed Al Nahyan", "2022-09-15", "Business", 30.50)
ebook3 = Ebook("Echoes of the Past", "Fatima Al Mansoori", "2021-03-22", "Historical Fiction", 18.75)

catalog = Catalog("C002", [ebook1, ebook2, ebook3], "2024-11-01", 3, "Majestic Reads Store")

# Display catalog information
print("Initial Catalog:")
for ebook in catalog.get_ebooks():
    print(ebook)

# Create a customer
customer1 = Customer("Aisha", "555-5678", True, "aisha@example.com", "456 Market Street")
print("\nCustomer Details:")
print(customer1)

# Create a cart for the customer and add items
cart = Cart(customer1, [ebook1, ebook3], 0, False, "2024-11-05")
cart_total = ebook1.get_price() + ebook3.get_price()
cart.set_total_price(cart_total)
print("\nCart Details:")
print(cart)

# Apply discounts if applicable
discount = Discount("D002", "Loyalty Member Discount", 10, "Loyalty program", True)
if customer1.get_loyalty_member() and discount.get_is_active():
    discount_amount = (cart.get_total_price() * discount.get_percentage()) / 100
    new_total = cart.get_total_price() - discount_amount
    cart.set_total_price(new_total)
    cart.set_discount_applied(True)

# Display updated cart total
print("\nUpdated Cart Total after Loyalty Discount:")
print("Total Price: $" + str(cart.get_total_price()))

# Create an order
order = Order("O002", cart, "Processing", "Pending", "Not delivered")
print("\nOrder Details:")
print(order)

# Generate an invoice
vat_rate = 8  # 8% VAT
vat_amount = (cart.get_total_price() * vat_rate) / 100
total_after_tax = cart.get_total_price() + vat_amount
invoice = Invoice("INV002", order, cart.get_total_price(), total_after_tax, vat_rate)

# Display invoice details
print("\nInvoice Details:")
print(invoice)
print("Total before tax: $" + str(invoice.get_total_before_tax()))
print("VAT amount: $" + str(vat_amount))
print("Total after tax: $" + str(invoice.get_total_after_tax()))

# Create and display store information
store = Store("Majestic Reads Store", "Online", "987-654-3210", catalog, True)
print("\nStore Details:")
print(store)
