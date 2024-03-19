# 3/14/24
# CSC-221
# Jahan P
# M1Pro - main

import csv
from classes import Customer, Product, Order

def read_customers(file_path):
    customers = []
    with open(file_path, 'r') as file:
        first_line = file.readline()  # Read the first line
        if first_line.strip(): # Skip the header line
            for line in file:
                cusId, name, email, isPremium = line.strip().split(',')
                customers.append(Customer(int(cusId), name, email, bool(isPremium)))
    return customers

def read_products(file_path):
    products = []
    with open(file_path, 'r') as file:
        first_line = file.readline()  # Read the first line
        if first_line.strip():   
            for line in file:
                product_id, rest = line.strip().split(',', 1)
                name, price = rest.rsplit(',', 1)
                price = price.strip('$')
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
