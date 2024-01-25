# determine the total cost 
# 1/23/23
# CSC121 M1Lab2– Review
# Jahan p


def calc_tax():
    #start with total tax  = 0
    total_tax = 0 
    #get number of items from user
    item_quantity = int(input("Enter number of items: "))
    # "CPI" = cost per item - get from user 
    CPI = float(input("Enter the cost for your item(s) (enter a decimal): "))
    #calc the cost of the item(s)
    item_cost = item_quantity*CPI
    #"TCOAI" = total cost of all items - finsish calc
    TCOAI = total_tax + item_cost
    return TCOAI

def main():
    more_items = "y"
    #while loop to keep the program going
    while more_items == "y":
        TCOAI = calc_tax()
        more_items = input("Do you want to add more items (y/n)? ")
    # cacl everything after u break from the loop
    tax_rate = float(input("Enter your tax rate (%) (enter a decimal): "))

    sales_tax = (tax_rate/100)*TCOAI

    subtotal = sales_tax + TCOAI

    print(f"Total cost (pre-tax):  ${TCOAI:.2f}")
    print(f"Sales tax:  ${sales_tax:.2f}")
    print(f"Total cost (with tax):  ${subtotal:.2f}")

if __name__ == "__main__":
    main()
