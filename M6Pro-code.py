import csv

# Function to load data from CSV file
def load_data(file_name):
    data = []
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header
        for row in csv_reader:
            data.append({'year': row[0], 'team': row[1]})
    return data

# Function to capitalize team names
def capitalize_team_name(team_name):
    return ' '.join(word.capitalize() for word in team_name.split())

# Function to search for the number of times a team won
def search_team_wins(team_name, data):
    wins = 0
    years_won = []
    for item in data:
        if item['team'] == team_name.lower():
            wins += 1
            years_won.append(item['year'])
    return wins, years_won

# Function to search for the winning team in a specific year
def search_year_winner(year, data):
    for item in data:
        if item['year'] == year:
            return capitalize_team_name(item['team'])
    return None

# Function to create a text file with team names and number of wins
def create_text_file(data):
    team_wins = {}
    for item in data:
        team = capitalize_team_name(item['team'])
        if team in team_wins:
            team_wins[team] += 1
        else:
            team_wins[team] = 1
    
    with open('WorldSeriesWinnersSummary.txt', 'w') as file:
        file.write(f"{'Team':<20}{'Wins':<10}\n")
        for team, wins in team_wins.items():
            file.write(f"{team:<20}{wins:<10}\n")

# Main function
def main():
    file_name = 'WorldSeriesWinners.csv'
    data = load_data(file_name)

    while True:
        print("\nMenu:")
        print("1. Search for a team's wins")
        print("2. Search for the winner in a specific year")
        print("3. Create a text file with team wins summary")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            team_name = input("Enter the name of the team: ").lower()
            wins, years_won = search_team_wins(team_name, data)
            print(f"{capitalize_team_name(team_name)} won {wins} times.")
            if years_won:
                print("Years won:", ', '.join(years_won))
        elif choice == '2':
            while True:
                year = input("Enter the year (4 digits): ")
                if len(year) != 4 or not year.isdigit():
                    print("Please enter a valid 4-digit year.")
                else:
                    winner = search_year_winner(year, data)
                    if winner:
                        print(f"The winner of {year} was {winner}.")
                    else:
                        print(f"No data available for the year {year}.")
                    break
        elif choice == '3':
            create_text_file(data)
            print("Text file created successfully: WorldSeriesWinnersSummary.txt")
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
