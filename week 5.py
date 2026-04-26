orders = []

def add_order():
    order = {
        "id": len(orders) + 1,
        "customer": input("Customer: "),
        "product": input("Product: "),
        "qty": int(input("Quantity: ")),
        "price": float(input("Price: ")),
        "status": "Placed"
    }
    orders.append(order)

def view_orders():
    for o in orders:
        print(o)

add_order()
view_orders()
