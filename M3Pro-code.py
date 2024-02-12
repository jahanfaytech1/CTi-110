# num of infected
# 2/1/24
# CSC121 M3Pro– List
# Jahan P

#"ROS" = rate of spread
from functions import calcI, display_table

def main():
    num_infected = int(input("Enter how many people are currently infected?: "))
    week = list(range(1, 9))
    rate_no_vac = [3, 3, 3, 3, 3, 3, 3, 3]
    rate_vac = [3, 3, 3, 3, 0.8, 0.8, 0.8, 0.8]

    scenario1 = calcI(num_infected, rate_no_vac)
    scenario2 = calcI(num_infected, rate_vac)

    display_table(week, scenario1, scenario2)
if __name__ == "__main__":
    main()
