"""
CP1404/CP5632 Practical
Wimbledon Program
"""

"""
Wimbledon
Estimate: 60 minutes
Actual:  243 minutes
"""


FILENAME = "wimbledon.txt"


def main():
    champion_to_wins = {}
    line_of_record = load_data()
    del line_of_record[0]
    extract_winner_from_file(champion_to_wins, line_of_record)
    print("Wimbledon Champions:")
    for winner, count in champion_to_wins.items():
        print(f"{winner} {count}")
    extract_country_from_file(line_of_record)


def load_data():
    """Read data from file"""
    in_file = open(FILENAME, encoding="utf-8-sig")
    lines = [line.strip().split(",") for line in in_file]
    in_file.close()
    return lines


def extract_winner_from_file(champion_to_wins, line_of_record):
    """Extract winners from each year in file"""
    winners = [champion[2] for champion in line_of_record]
    for winner in winners:
        if winner in champion_to_wins:
            champion_to_wins[winner] += 1
        else:
            champion_to_wins[winner] = 1


def extract_country_from_file(line_of_record):
    """Extract winning countries from each year in file"""
    countries_won = set([country[1] for country in line_of_record])
    print(f"These {len(countries_won)} countries have won Wimbledon:")
    print(", ".join(sorted(countries_won)))


main()
