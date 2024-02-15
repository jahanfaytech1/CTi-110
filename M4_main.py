# Tsion Pettiford
#2/06/2024
#using nested dictionaries
'''MAIN'''

from M4_functions import * #imports all function

def main():
    '''student_registry = getStudentsReg()
     # call the function
    display_content(student_registry)


    #create a loop to control the program'''
    option = 1
    students = getStudentReg()
    while option != 5:
        display_menu()
        option = int(input("Enter a choice to get started"))
        
        if option == 1:
            display_content(students)
            
        if option == 2:
            course = input("Enter the course to get the student roster: ")
            for each in (display_roster(students, course)):
                print(each)
        if option == 3:
            major = input("Enter the major to get the students with that major: ")
            for each in (getMajor(students, major)):
                print(each)
        if option == 4:
            stuID = input("Enter the student ID to get the student with that ID: ")
            for each in (getID(students, stuID)):
                print(each)
        if option == 5:
            print("The program has ended")
    





if __name__ == "__main__":
    main()
