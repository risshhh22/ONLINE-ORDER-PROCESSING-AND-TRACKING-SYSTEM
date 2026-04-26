import pandas as pd

data = [
    {"product": "Shoes", "qty": 2, "price": 1000},
    {"product": "Shirt", "qty": 1, "price": 500}
]

df = pd.DataFrame(data)
df["total"] = df["qty"] * df["price"]

print(df)
print("Total Revenue:", df["total"].sum())