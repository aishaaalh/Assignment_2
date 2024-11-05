from catalog import Catalog
from customer import Customer
from cart import Cart
from order import Order
from discount import Discount
from invoice import Invoice
from ebook import Ebook

# Test Case 1: Add/Modify/Remove a new e-book to the e-bookstore's catalog (bulk discount scenario)
def test_case_1_catalog_operations():
    # Create initial catalog
    ebook1 = Ebook("Mystic Tides", "Ali Al Muhairi", "2023-01-20", "Fantasy", 12.00)
    ebook2 = Ebook("The Desert Path", "Fatima Al Suwaidi", "2022-08-10", "Adventure", 15.50)
    catalog = Catalog("C001", [ebook1], "2024-11-01", 1, "Grand Library")
    
    # Add a new e-book
    catalog.add_ebook(ebook2)
    print("\nAfter adding 'The Desert Path':")
    for ebook in catalog.get_ebooks():
        print(ebook)
    
    # Modify the added e-book
    ebook3 = Ebook("The Desert Path - Revised", "Fatima Al Suwaidi", "2022-12-10", "Adventure", 17.00)
    catalog.modify_ebook("The Desert Path", ebook3)
    print("\nAfter modifying 'The Desert Path':")
    for ebook in catalog.get_ebooks():
        print(ebook)
    
    # Remove the e-book
    catalog.remove_ebook("The Desert Path - Revised")
    print("\nAfter removing 'The Desert Path - Revised':")
    for ebook in catalog.get_ebooks():
        print(ebook)

# Test Case 2: Adding items to the cart and applying a bulk discount (success case)
def test_case_2_bulk_discount():
    # Create e-books
    ebook1 = Ebook("Desert Chronicles", "Aisha Al Shamsi", "2023-06-01", "History", 20.00)
    ebook2 = Ebook("The Falcon's Journey", "Hassan Al Rashid", "2023-08-15", "Fiction", 18.00)
    ebook3 = Ebook("Legacy of Sands", "Mouza Al Habtoor", "2023-03-11", "Drama", 22.00)
    ebook4 = Ebook("Mystic Legends", "Zayed Al Khaili", "2022-05-22", "Fantasy", 19.00)
    ebook5 = Ebook("Whispers of Time", "Ali Al Mazrouei", "2023-09-12", "Thriller", 24.00)
    ebook6 = Ebook("Ocean's Call", "Salma Al Derei", "2024-02-14", "Adventure", 21.00)

    # Create a customer and cart
    customer = Customer("Khalifa", "555-9999", False, "khalifa@example.com", "101 Seaside Road")
    cart = Cart(customer, [ebook1, ebook2, ebook3, ebook4, ebook5, ebook6], 0, False, "2024-11-05")
    
    # Set initial total price for the cart
    cart_total = sum([ebook.get_price() for ebook in cart.get_items()])
    cart.set_total_price(cart_total)
    
    # Apply a bulk discount (20% for 5 or more items)
    bulk_discount = Discount("D002", "Bulk Purchase Discount", 20, ["bulk"], True)
    if len(cart.get_items()) >= 5 and bulk_discount.get_is_active():
        discount_amount = (cart.get_total_price() * bulk_discount.get_percentage()) / 100
        new_total = cart.get_total_price() - discount_amount
        cart.set_total_price(new_total)
        cart.set_discount_applied(True)

    print("\nCart Total after Bulk Discount:")
    print("Total Price: $" + str(cart.get_total_price()))

# Test Case 3: Fail case - applying an inactive discount
def test_case_3_inactive_discount():
    # Create e-books and cart
    ebook1 = Ebook("Echoes of Eternity", "Fatima Al Darmaki", "2023-10-01", "Poetry", 25.00)
    customer = Customer("Hamad", "555-1234", True, "hamad@example.com", "456 Palm Street")
    cart = Cart(customer, [ebook1], 0, False, "2024-11-05")
    
    # Set initial total price for the cart
    cart.set_total_price(ebook1.get_price())

    # Create an inactive discount
    inactive_discount = Discount("D003", "Seasonal Discount", 15, ["loyalty"], False)
    
    # Try applying the inactive discount
    if customer.get_loyalty_member() and inactive_discount.get_is_active():
        discount_amount = (cart.get_total_price() * inactive_discount.get_percentage()) / 100
        new_total = cart.get_total_price() - discount_amount
        cart.set_total_price(new_total)
        cart.set_discount_applied(True)
    else:
        print("\nInactive discount applied (should not change the total):")
        print("Total Price: $" + str(cart.get_total_price()))

# Run test cases
print("Test Case 1: Catalog Operations")
test_case_1_catalog_operations()

print("\nTest Case 2: Bulk Discount")
test_case_2_bulk_discount()

print("\nTest Case 3: Inactive Discount")
test_case_3_inactive_discount()
