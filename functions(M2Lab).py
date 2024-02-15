# ATM waiting time
# 1/25/23
# CSC121 M2Lab– Function Review
# Jahan Powell


#function for inputs 

def getInputs():

    #get inputs from the user
    
    #"AAR" = average arrival rates
    AAR = int(input("Enter the average arrival rate: "))
    
    #"AsR" = average service rates
    ASR = int(input("Enter the average service rate: "))
    return AAR, ASR


#function for wait time 

def calcWT(AAR, ASR):
    #"AWT" = average wait time
    AWT = 1/(ASR - AAR)-1/ASR

    #"ACIL" = average customers in line
    ACIL = AAR/(ASR-AAR)-AAR/ASR
    return AWT, ACIL

def DisplayResult(AWT):
    #turn hours into minutes
    #t"AWTM" = average time 'minutes'
    AWTM = AWT*60
    return AWTM

def menuInput():
    print("-------menu-------")
    print("1) Calulate wait time")
    print("2) Exit")
    print("------------------")
    menu = input("what do you want to do?(1 or 2)")
    return menu
