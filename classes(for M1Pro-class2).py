# 3/14/24
# CSC-221
# Jahan P
# M1Pro - funtcions

# classes.py

class Customer:
    def __init__(self, cusId, name, email, isPremium):
        self.cusId = cusId
        self.name = name
        self.email = email
        self.isPremium = isPremium
        if self.isPremium:
            self.membership_id = f"{cusId}_100"

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class Order:
    def __init__(self, customer, product, quantity):
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.discount = 0.1 if customer.isPremium else 0
        self.total = product.price * quantity
        
    def calculate_total(self):
        subtotal = self.product.price * self.quantity
        discount_amount = subtotal * self.discount
        return subtotal - discount_amount
