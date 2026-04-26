orders = []

def add_order():
    name = input("Customer: ").lower()
    product = input("Product: ").lower()
    qty = int(input("Quantity: "))
    price = float(input("Price: "))
    orders.append([name, product, qty, price])

def view_orders():
    for o in orders:
        print(o)

def search():
    key = input("Search customer: ").lower()
    for o in orders:
        if key in o[0]:
            print(o)

while True:
    print("\n1.Add 2.View 3.Search 4.Exit")
    ch = input()

    if ch == "1":
        add_order()
    elif ch == "2":
        view_orders()
    elif ch == "3":
        search()
    else:
        break