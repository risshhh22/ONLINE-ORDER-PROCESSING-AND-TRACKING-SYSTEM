from storage.json_store import save, load

orders = load()

orders.append({"id": 1, "name": "Rishi"})
save(orders)