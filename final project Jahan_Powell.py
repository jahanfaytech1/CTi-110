#reading data from a file
# 3/5/24
# CSC121 Final Project
# Jahan P

import csv


class Student():
    def __init__(self, stuID, first_name, last_name):
                 self.stuID = stuID
                 self.first_name = first_name
                 self.last_name = last_name
                 self.active_status = True

    def __repr__(self):
        return (f"\nStudent ID: {self.stuID} \nFirst Name: {self.first_name} \nLast Name: {self.last_name} \nActive Status: {self.active_status}")
                
def read_content():
    students = []

    with open("StudentInfo.csv", 'r' ) as file:
        reader = csv.reader(file)
        next(reader)
            #loop through each line in file
        for row in reader:
            last_name = row[0]
            first_name = row[1]
            stuID = row[2]

            #create student object
            students.append(Student(stuID, first_name, last_name))
        return students

def show_menu():
    print('''--------------Menu-----------------------------------
1) Display all Student Records
2) Add a New Student Record
3) Search for Student by Id
4) Delete a Student Record (set to inactive)
5) Write to CSV
6) Exit
---------------------------------------------------------
''')

def add_student(students):
    stuID = input("Enter student ID: ")
    first_name = input("Enter students first name: ")
    last_name = input("Enter students last name: ")
    new = Student(stuID, first_name, last_name)
    
    students.append(new)
    return students

def search_id(students):
    find_id = input("Enter the ID of your student: ")
    for i in students:
        if i.stuID == find_id:
            return i

def set_inactive(students):
    stu_OBJ = search_id(students)
    stu_OBJ.active_status = False
    print(f"Student {stu_OBJ.first_name} {stu_OBJ.last_name} was set to inactive")

def write_file(students):
    with open("output.csv", 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["studID", "first_name", "last_name", "active_status"])
        for obj in students:
            writer.writerow([obj.stuID, obj.first_name, obj.last_name, obj.active_status])
    print("output.csv has been created")


def main():
    students = read_content()
    option = 0
    while option != 6:
        show_menu()
        option = int(input("Enter an option: "))
        if option == 1:
            for i in students:
                     print(i)
                     
        elif option == 2:
            add_student(students)
        elif option == 3:
            print(search_id(students))
        elif option == 4:
            set_inactive(students)
        elif option == 5:
            write_file(students)
        elif option == 6:
            print("GOODBYEEE!!!")
            break

        else:
            print("\nyour option is invalid\n")


if __name__ == "__main__":
    main()
