import random
from . import pricing

def generate_order_id(customer_name):
    
    prefix = customer_name[:3].upper()
    suffix = str(random.randint(10000,99999))
    return prefix + suffix
    
def calculate_total(price, discount_percent, tax_rate):
    discounted = pricing.calculate_discounterd_price(price, discount_percent)
    tax = pricing.calculate_tax(discounted, tax_rate)
    total = discounted + tax
    return total