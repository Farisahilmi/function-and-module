def calculate_discounterd_price(price, discount_percent):
    return price - (price * discount_percent/ 100)

def calculate_tax(price, tax_rate):
    return price * tax_rate / 100
