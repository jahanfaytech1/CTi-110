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
            patient_id, height, weight = line.strip().split(',')
            BMI = calcBMI(height, weight)
            if BMI is not None:
                patient_data.append({"patient_id":patient_id, "height":height, "weight":weight, "BMI":BMI})
            else:
                print(f"Patient ID: {patient_id} is incorrect or doesnt exist.")
    return patient_data


def WTBF(patient_id, BMI):
    with open('patient_data.txt', 'a') as bmi_file:
        bmi_file.write(f"patient ID: {patient_id}, BMI: {BMI}\n")

def CNF(file_name):
    with open('patient_data.txt', 'w') as new_file:
        #new_file.write("\n")
        new_file.write("P0123,66,150 \n")
        new_file.write("P4354,68,164 \n")

def getID(patient_data, patient_id):
    for patient in patient_data:
        TPID = patient["patient_id"]
        if TPID == patient_id:
            print(f"Patient ID: {patient_id}, BMI: {patient['BMI']:.2f}")
            WTBF(patient_id, patient['BMI'])
            return True
    print(f"Patient ID: {patient_id} not found.")   
    return False


def main():
    file_name = 'patient_data.txt'
    CNF(file_name)
    patient_data = Process_PD(file_name)
    #print(patient_data)
    TPID = input("Enter the ID of the patient you want to see: ")
    getID(patient_data, TPID)


if __name__ == "__main__":
    main()
