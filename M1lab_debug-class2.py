# 3/14/24
# CSC-221
# Jahan P
# M1Lab1 - main


from person import Person

class Employee(Person):
    def __init__(self, firstName, lastName, salary, part_full_time, status):
        super().__init__(lastName, firstName)
        self.part_full_time = part_full_time
        self.salary = salary
        self.status = status

    def set_position(self, position):
        self.__position = position

    def get_position(self):
        return self.__position

    def set_part_full_time(self):
        return self.part_full_time
     
    def get_salary(self):
        return self.salary


def main():
    EXIT = "3"
    choice = ""
  
    while choice != EXIT:
        x = 0
        print("Menu")
        print("----------------")
        print("1. Enter Employee Info and write to .txt and .csv files:" 
              + "\n2. Read Employee Info from .txt and csv files (if existing)" 
              + "\n3. Exit Program\n")
        choice = input("Please enter your choice: ")

        header = "First Name Last Name Email(Company Email) Salary Part/Full"
                    
        if choice == "1":
            # Write to txt and csv
            outFile_txt = open("employees.txt", "w")
            outFile_txt.write(header + "\n")
            outFile_csv = open("employees.csv", "w")
            outFile_csv.write(header.replace(" ", ",") + "\n")

            empNum = int(input("How many employee info would you like to enter? >"))
            for i in range(empNum):
                first = input("First Name: ")
                last = input("Last Name: ")
                position = input("Position: ")
                part_full = input("Part/Full Time: ")
                salary = input("Salary: ")

                employee = Employee(first, last, salary, part_full, "")
                employee.set_position(position)

                # Writing to txt file
                outFile_txt.write(f"{employee.firstName} {employee.lastName} {employee.get_email()} {employee.salary} {employee.part_full_time}\n")

                # Writing to csv file
                outFile_csv.write(f"{employee.firstName},{employee.lastName},{position},{employee.part_full_time},{employee.salary}\n")

            outFile_txt.close()
            outFile_csv.close()

        elif choice == "2":
            try:
                with open("employees.txt", "r") as inFile_txt:
                    print("Reading from employees.txt:")
                    print(inFile_txt.read())
            except FileNotFoundError:
                print("employees.txt not found!")
            try:
                with open("employees.csv", "r") as inFile_csv:
                    print("\nReading from employees.csv:")
                    print(inFile_csv.read())
            except FileNotFoundError:
                print("employees.csv not found!")

        elif choice == EXIT:
            print("Closing program! Good bye.")
        else:
            print("This is not a valid option! Please choose from the menu.\n\n")

if __name__ == "__main__":
    main()




