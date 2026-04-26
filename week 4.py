orders = []

def calculate_total(qty, price):
    return qty * price

def add_order():
    name = input("Customer: ")
    product = input("Product: ")
    qty = int(input("Quantity: "))
    price = float(input("Price: "))

    total = calculate_total(qty, price)
    orders.append([name, product, qty, price, total])

def view_orders():
    for o in orders:
        print(o)

while True:
    print("\n1.Add 2.View 3.Exit")
    ch = input()

    if ch == "1":
        add_order()
    elif ch == "2":
        view_orders()
    else:
        break