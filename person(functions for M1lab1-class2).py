# 3/14/24
# person class
# Jahan P

class Person:
    def __init__(self, lastName, firstName):
        self.firstName = firstName
        self.lastName = lastName
        self.email = lastName[:5] + "_" + firstName[0:] + "@abc_shipping.com"

    def set_lastName(self, lastName):
        self.lastName = lastName
        
    def get_lastName(self):
        return self.lastName
    
    def set_firstName(self, firstName):
        self.firstName = firstName
        
    def get_firstName(self):
        return self.firstName

    def get_email(self):
        return self.email
