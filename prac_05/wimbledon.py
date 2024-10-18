"""
CP1404/CP5632 Practical
Wimbledon Program
"""

"""
Wimbledon
Estimate: 60 minutes
Actual:      minutes
"""

champion_to_wins = {}

# in_file = open('wimbledon.txt', 'r')
with open("wimbledon.txt", "r", encoding="utf-8-sig") as in_file:
    lines = [line.strip().split(",") for line in in_file]
    del lines[0]
    winners = [champion[2] for champion in lines]
    for winner in winners:
        if winner in champion_to_wins:
            champion_to_wins[winner] += 1
        else:
            champion_to_wins[winner] = 1

countries_won = set([line[1] for line in lines])

print("Wimbledon Champions:")
for winner, count in champion_to_wins.items():
    print(f"{winner} {count}")

print(f"These {len(countries_won)} countries have won Wimbledon")
print(", ".join(sorted(countries_won)))


in_file.close()



