# determine the total cost 
# 2/1/24
# CSC121 M2Pro – Review
# Jahan p

# all the functions

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

def AddMore():
    #while loop to keep going
        TCOAI = calc_tax()
        more_items = input("Do you want to add more items (y/n)? ")
        return TCOAI, more_items
         


def calcTC(TCOAI):
    tax_rate = float(input("Enter your tax rate (%) (enter a decimal): "))
     
    sales_tax = (tax_rate/100)*TCOAI
     
    subtotal = sales_tax + TCOAI
     
    return sales_tax, subtotal
