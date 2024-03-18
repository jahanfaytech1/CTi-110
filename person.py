# 3/14/24
# person class
# Jahan P

class Person:
    def __init__(self, lastName, firstName):
        self.firstName = firstName
        self.lastName = lastName
        self.email = lastName[:5] + "_" + firstName[0:] + "@abc_shipping.com"

    def set_lastName(self, lastName):
        self.__lastName = lastName
        
    def get_lastName(self):
        return self.__lastName
    
    def set_firstName(self, firstName):
        self.__lastName = firstName
        
    def get_firstName(self):
        return self.__firstName

    def get_email(self):
        return self.email

'''dave = Person("Miller", "Dave")
print(dave.get_email())'''
