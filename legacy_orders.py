"""
legacy_orders.py  -  Loafly's "it ran fine on my laptop" script.

This is the BEFORE. It works for the happy rows, but look at the problems:
  - the price cleaning is copy-pasted inline
  - the discount is a magic number typed into the logic
  - the API key is sitting right here in the code
  - it uses print(), has no error handling, and no retry
  - everything lives in one file

It also crashes the first time it meets an order with a missing price,
which is exactly the kind of 2am breakage this session is about.

Run:  python legacy_orders.py
"""
import csv

def clean_price(price):
    """Clean the price string and convert to float."""
    cleaned=float(price.replace(",", "").strip())  # remove leading/trailing whitespace
    return float(cleaned)

def apply_discount(price, percent):
    """Apply a discount to the price."""
    final_price = price - (price * percent / 100)
    return final_price 

# read today's raw orders
rows = []
with open("raw_orders.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        rows.append(row)

# group the item rows into orders
orders = {}
for row in rows:
    oid = row["order_id"]
    if oid not in orders:
        orders[oid] = {"customer": row["customer"], "items": []}
    orders[oid]["items"].append((row["item_name"], row["item_price"]))

# process every order
for oid, o in orders.items():
    total = 0
    for name, price in o["items"]:
        total = total + clean_price(price)   # cleaning, copy-pasted inline
    total = apply_discount(total, 10)                     # discount, magic number
    api_key = "YOUR_API_KEY_HERE"                   # secret, sitting in the code (!)
    print("saving order", oid, "for", o["customer"], "total", total)   # no logging, no retry


print(clean_price("1,250.50"))
print(apply_discount(1000, 10))