
# Raw dataset provided in the problem
raw_orders = [
    " ORD101 , Alice , Electronics , 250.0 , 10% ",
    "ORD102, Bob , Books , 45.0 , 0% ",
    " ORD103, Alice , Books , 30.0 , 5% ",
    "ORD104, CHARLIE , Electronics , 120.0 , 10% ",
    "ORD105, Bob , Electronics , 300.0 , 15% ",
    "ORD106, Invalid_User , Toys , -50.0 , 0% "
]

# ==========================================
# Part 1: Data Parsing, Cleaning & Nested Aggregation
# ==========================================

valid_records = []
customer_breakdown = {}

for record in raw_orders:
    # 1. Split fields and clean whitespace
    fields = [f.strip() for f in record.split(',')]
    
    order_id = fields[0]
    customer = fields[1].title()  # Standardize customer names to Title Case
    category = fields[2]
    
    # 2. Parse price and discount
    price = float(fields[3])
    
    # Discard record if price is non-positive (<= 0.0)
    if price <= 0.0:
        continue
        
    # Strip '%' sign and convert to float
    discount_pct = float(fields[4].replace('%', ''))
    
    # 3. Compute the final net price
    net_price = price * (1 - discount_pct / 100)
    
    # 4. Store valid record as a tuple
    valid_records.append((order_id, customer, category, net_price))
    
    # 5. Aggregate net spend into nested dictionary
    if customer not in customer_breakdown:
        customer_breakdown[customer] = {}
        
    if category not in customer_breakdown[customer]:
        customer_breakdown[customer][category] = 0.0
        
    customer_breakdown[customer][category] += net_price

# 6. Print Part 1 outputs
print("Part 1 - Customer Category Breakdown and valid records:")
print("\nValid Records")
print(valid_records)
print("\nCustomer Category Breakdown")
print(customer_breakdown)


# ==========================================
# Part 2: High-Value Order Extraction
# ==========================================

# 1 & 2. Extract and store order IDs where net price strictly exceeds 100.0
high_value_orders = [order_id for order_id, customer, category, net_price in valid_records if net_price > 100.0]

# 3. Print Part 2 outputs
print("\n" + "="*40)
print("Part 2: High-Value Orders")
print(f"High-Value Net Orders (> 100): {high_value_orders}")