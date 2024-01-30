# ATM waiting time
# 1/25/23
# CSC121 M2Lab– Function Review
# Jahan Powell

from functions import getInputs
from functions import calcWT
from functions import DisplayResult
from functions import menuInput
   
def main():
    menu = menuInput()
    while menu == "1":
        AAR, ASR = getInputs()
        AWT, ACIL = calcWT(AAR, ASR)
        AWTM = DisplayResult(AWT)
    
        print(f"your average wait time is {AWTM:.1f} minutes")
        print(f"the average customers in line is {ACIL:.2f} people")
        menu = menuInput()
    if menu == "2":
            print("Thank you for using our site!!")
    else:
        print("you didnt choose one of the options")
        print(":(")

if __name__ == "__main__":
    main()
