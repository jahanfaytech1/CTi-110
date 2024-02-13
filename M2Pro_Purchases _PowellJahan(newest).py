# determine the total cost 
# 2/1/24
# CSC121 M2Pro – Review
# Jahan p

# import functions from other file

from functions import calc_IC, calcTC


# main program

def main():
    TCOAI = 0
    more_items = "y"
    while more_items == "y":
        TCOAI, more_items = calc_IC(TCOAI)

    sales_tax, subtotal = calcTC(TCOAI)
    print(f"Total cost (pre-tax):  ${TCOAI:.2f}")
    print(f"Sales tax:  ${sales_tax:.2f}")
    print(f"Total cost (with tax):  ${subtotal:.2f}")
    
    
if __name__ == "__main__":
    main()

