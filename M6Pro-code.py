import csv

def read_csv_file():
    try:
        with open('WorldSeriesWinners.csv', 'r') as file:
            reader = csv.reader(file)
            data = {rows[0]: rows[1] for rows in reader}
        return data
    except FileNotFoundError:
        print("Error: File 'WorldSeriesWinners.csv' not found.")
        exit()

def search_team(team_name):
    data = read_csv_file()
    count = 0
    years = []

    for year, name in data.items():
        if name == team_name:
            count += 1
            years.append(year)

    if count == 0:
        print(f"The team '{team_name.capitalize()}' has never won the World Series.")
    else:
        print(f"The team '{team_name.capitalize()}' has won {count} time(s) in the following year(s): {', '.join(years)}")

def get_winner_for_year(year):
    if not year.isdigit() or len(year) != 4:
        print("Error: Please enter a valid 4-digit year.")
        return

    data = read_csv_file()
    if year in data:
        print(f"In {year}, the winner was '{data[year].capitalize()}'.")
    else:
        print(f"No data available for the year {year}.")

def generate_winner_file():
    data = read_csv_file()
    team_counts = {}
    for team in data.values():
        team = team.capitalize()
        team_counts[team] = team_counts.get(team, 0) + 1

    with open('WorldSeriesWinners.txt', 'w') as file:
        file.write("Team\t\tNumber of Wins\n")
        file.write("--------------------------\n")
        for team, count in sorted(team_counts.items()):
            file.write(f"{team.ljust(20)}{str(count).rjust(15)}\n")




def main():
    print("Welcome to World Series Winners Analyzer!")
    while True:
        print("\nMenu:")
        print("1. Search for a team")
        print("2. Get the winner for a specific year")
        print("3. Generate a text file with all winners and their counts")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            team_name = input("Enter the name of the team: ").lower()
            search_team(team_name)
        elif choice == '2':
            year = input("Enter the year: ")
            get_winner_for_year(year)
        elif choice == '3':
            generate_winner_file()
            print("File 'WorldSeriesWinners.txt' has been generated.")
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
