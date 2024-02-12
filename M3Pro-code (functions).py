# num of infected
# 2/1/24
# CSC121 M3Pro– List
# Jahan P

#functions

def calcI(num_infected, ROS):
    '''Takes in an integer and a list. Returns a list.'''
    infections = [num_infected]
    for rate in ROS:
        num_infected *= rate
        infections.append(num_infected)
    return infections

def display_table(week, scenario1, scenario2):
    '''Displays the table of results.'''
    print("Week\tScenario 1\tScenario 2")
    print("--------------------------------")
    for i in range(len(week)):
        print(f"{week[i]}\t{scenario1[i]}\t\t{scenario2[i]}")
