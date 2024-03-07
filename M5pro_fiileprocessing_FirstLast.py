# A brief description of the project
# Date
# CSC121 M5Pro
# Your Name

import csv

# Function to read transactions from the CSV file
def read_transactions():
    with open('sales.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Function to add new transactions to the CSV file
def add_transaction():
    transaction_num = input("Enter transaction number: ")
    sale_date = input("Enter sale date (yyyy-mm-dd): ")
    product_id = input("Enter product ID: ")
    customer_num = input("Enter customer number: ")
    units_sold = input("Enter units sold: ")
    price_per_unit = input("Enter price per unit: ")

    with open('sales.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([transaction_num, sale_date, product_id, customer_num, units_sold, price_per_unit])

# Function to display total sales for each product
def total_sales_per_product():
    products = {}
    with open('sales.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            product_id = row[2]
            units_sold = int(row[4])
            price_per_unit = float(row[5])
            total_sales = units_sold * price_per_unit
            if product_id in products:
                products[product_id] += total_sales
            else:
                products[product_id] = total_sales
    
    print("Total Sales for Each Product:")
    for product, sales in products.items():
        print(f"Product ID: {product}, Total Sales: ${sales:.2f}")

# Function to display total units and total sales for each customer
def total_units_and_sales_per_customer():
    customers = {}
    with open('sales.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            customer_id = row[3]
            units_sold = int(row[4])
            price_per_unit = float(row[5])
            total_sales = units_sold * price_per_unit
            if customer_id in customers:
                customers[customer_id][0] += units_sold
                customers[customer_id][1] += total_sales
            else:
                customers[customer_id] = [units_sold, total_sales]
    
    print("Total Units and Total Sales for Each Customer:")
    print("Customer ID\tTotal Units Sold\tTotal Sales")
    for customer, data in customers.items():
        print(f"{customer}\t\t{data[0]}\t\t\t${data[1]:.2f}")

# Function to write total sales for each customer to a .txt file
def write_sales_per_customer():
    customers = {}
    with open('sales.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            customer_id = row[3]
            units_sold = int(row[4])
            price_per_unit = float(row[5])
            total_sales = units_sold * price_per_unit
            if customer_id in customers:
                customers[customer_id][0] += units_sold
                customers[customer_id][1] += total_sales
            else:
                customers[customer_id] = [units_sold, total_sales]
    
    with open('sales_per_customer.txt', 'w') as file:
        file.write("Customer ID\tTotal Units Sold\tTotal Sales\n")
        for customer, data in customers.items():
            file.write(f"{customer}\t\t{data[0]}\t\t\t${data[1]:.2f}\n")

# Main function to implement menu-driven program
def main():
    while True:
        print("----------------MENU-------------------------")
        print("1) Read from existing list of transactions")
        print("2) Add new transactions to file")
        print("3) Display Total Sales for each Product")
        print("4) Display Total Units and Total Sales for each Customer")
        print("5) Exit")
        print("----------------------------------------------")
        choice = input("Enter your choice: ")

        if choice == '1':
            read_transactions()
        elif choice == '2':
            add_transaction()
        elif choice == '3':
            total_sales_per_product()
        elif choice == '4':
            total_units_and_sales_per_customer()
            write_sales_per_customer()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
