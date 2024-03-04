#reading data from a file
# 2/15/24
# CSC121 M5Lab
# Jahan P

def calcBMI(height, weight):
    try:
        height = float(height)
        weight = float(weight)
        BMI = weight/(height**2) * 703
        return BMI
    except ValueError:
        return none

def Process_PD(file_name):
    bmi_output_file = 'BMI.txt'
    patient_data = []
    with open(file_name, 'r') as file:
        for line in file:
            patient_id, hieght, weight = line.strip().split(',')
            BMI = calcBMI(hieght, weight)
            patient_data.append(patient_id)
        
    return patient_id, hieght, weight, BMI, patient_data


def WTBF(patient_id, BMI):
    with open('patient_data.txt', 'a') as bmi_file:
        bmi_file.write(f"patient ID: {patient_id}, BMI: {BMI}\n")

def CNF(file_name):
    with open('patient_data.txt', 'w') as new_file:
        #new_file.write("\n")
        new_file.write("P0123,66,150 \n")
        new_file.write("P4354,68,164 \n")

'''def getID(______):
   if BMI is not None:
            print(f"Patient ID: {patient_id}, BMI: {BMI:.2f}")
            WTBF(patient_id, BMI)
        else:
            print(f"Patient ID: {patient_id} height or weight is incorrect.")
    return ____'''


def main():
    file_name = 'patient_data.txt'
    CNF(file_name)
    patient_id, hieght, weight, BMI, patient_data = Process_PD(file_name)
    print(patient_data)
    



if __name__ == "__main__":
    main()
    
#this is completely wrong edit and change depending on the last assignment - jahan 
