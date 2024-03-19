# 3/14/24
# CSC-221
# Jahan P
# M1Lab1 - main

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
        self.total = product.price * quantity


# main.py
#from classes import Customer, Product, Order

def read_customers(file_path):
    customers = []
    with open(file_path, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            cusId, name, email, isPremium = line.strip().split(',')
            customers.append(Customer(int(cusId), name, email, bool(int(isPremium))))
    return customers

def read_products(file_path):
    products = []
    with open(file_path, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            product_id, name, price = line.strip().split(',')
            products.append(Product(int(product_id), name, float(price)))
    return products

def main():
    customers = read_customers('customers.csv')
    products = read_products('products.csv')

    while True:
        user_id = input("Enter your customer ID: ")
        customer = None
        for cus in customers:
            if cus.cusId == int(user_id):
                customer = cus
                break
        
        if customer:
            print(f"Welcome, {customer.name}!")
            product_id = input("Enter the product ID you want to purchase: ")
            product = None
            for prod in products:
                if prod.product_id == int(product_id):
                    product = prod
                    break
            
            if product:
                quantity = int(input("Enter the quantity you want to buy: "))
                order = Order(customer, product, quantity)
                with open('orders.txt', 'a') as f:
                    f.write(f"Customer ID: {customer.cusId}, Product: {product.name}, Quantity: {quantity}, Total: ${order.total}\n")
                print(f"Order placed! You need to pay ${order.total}.")
            else:
                print("Invalid product ID.")
        else:
            print("You are not a registered customer.")
        
        choice = input("Do you want to purchase more products? (yes/no): ")
        if choice.lower() != 'yes':
            print("Thank you for shopping with us!")
            break

if __name__ == "__main__":
    main()
