class Order:
    def __init__(self, oid, customer, product, qty, price):
        self.oid = oid
        self.customer = customer
        self.product = product
        self.qty = qty
        self.price = price
        self.status = "Placed"

    def total(self):
        return self.qty * self.price

    def display(self):
        print(self.oid, self.customer, self.product, self.total(), self.status)