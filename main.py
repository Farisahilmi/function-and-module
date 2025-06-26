from ecommerce.order import generate_order_id, calculate_total

customer_name = "Alex"
price = 100000
discount_percent = 20
tax_rate = 10

order_id = generate_order_id(customer_name)
total = calculate_total(price, discount_percent, tax_rate)

print(f"order id: {order_id}")
print(f"total to pay: {total}")