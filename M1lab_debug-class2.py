# 3/14/24
# CSC-221
# Jahan P
# M1Lab1 - main


from person import Person




class Employee(Person):
    def __init__(salary, part_full_time):
        
        self.name = firstName = lastName
        self.part_full_time = part_fullTime
        self.salary = salary
        self.status
    
   
    def set_position(self, position):
        self.__position = position

    def get_position(positon):
        self.__position

    def set_part_full_time():
        return part_full_time
     
    def get_salary(self):
        return self.__salary

        




def main():
  
    while choice !=  EXIT:
            
            x=0
            employee = Employee("","","","",0,"") 
        
           
            print("Menu")
            print("----------------")
            print("1. Enter Employee Info and write to .txt and .csv files: " 
                  + "\n2. Read Employee Info from .txt and csv files (if existing) " 
                  + "\n3. Exit Program/n")
            choice = input("Please enter your choice: ")
            
            
            header = "First Name Last Name Email(Company Email) Salary Part/Full"
                    

            if choice == 1:
                #Write to txt and csv
                outFile = open("employees.txt")
                
                
                outFile.writeline(header)
               

            
                outFile = open("employees")
         
                csvFile = outFile.writer()
                csvFile.writerows("First Name"+"Last Name"+"Position"+"Part/Full Time"+"Salary")
                
                
                empNum = int(input("How many employee info would you like to enter? >"))
                for i in empNum:
                   
                    first = input("First Name: ")
                    last = input("Last Name: ")
                    position = input("Position: ")
                    part_full = input("Part/Full Time: ")

                    # complete section here. create an instance of Employee then write instance information to a .txt AND a .csv file
                    
           
           
            if choice == "2":
                try:
                    inFile = open("employees") 
    
                except:
                    print("File Error! Please use option 1!")
    
                '''else:
                    #Read and display txt file content
                    #line break then read and display csv file content'''
                  
    
            elif choice == "3":
                print("Closing program! Good bye.")
               
            else:
                
                print("This is not a valid option! Please choose from the menu. \n\n")
            

    






