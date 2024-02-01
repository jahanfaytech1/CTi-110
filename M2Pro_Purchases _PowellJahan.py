# determine the total cost 
# 2/1/24
# CSC121 M2Pro – Review
# Jahan p

# import functions from other file

from functions import calc_tax
from functions import AddMore
from functions import calcTC


# main program

def main():
    more_items = "y"
    while more_items == "y":
        TCOAI, more_items = AddMore()

    sales_tax, subtotal = calcTC(TCOAI)
    print(f"Total cost (pre-tax):  ${TCOAI:.2f}")
    print(f"Sales tax:  ${sales_tax:.2f}")
    print(f"Total cost (with tax):  ${subtotal:.2f}")
    
    
if __name__ == "__main__":
    main()
