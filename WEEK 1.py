customer = input("Enter customer name: ")
product = input("Enter product name: ")
qty = int(input("Enter quantity: "))
price = float(input("Enter price per unit: "))

total = qty * price

print("\n--- BILL ---")
print("Customer:", customer)
print("Product:", product)
print("Quantity:", qty)
print("Total Amount: ₹", total)