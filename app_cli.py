from main import *
from dataclasses import dataclass

possible_rates = ["VoisinsDeZero", "Tier", "Orphelins", "Parity 1", "Parity 0", "Color R", "Color G", "Color B"]

@dataclass
class Player:
    name: str
    rate: RateType

players: List[Player] = []

def add_player(name, rate):
    players.append(Player(name, convert_string_to_rate(rate)))

def get_rate():
    str = input("Print new player rate:").strip()
    if str in possible_rates:
        return str
    while True:
        str = input("Print RIGHT new player rate:").strip()
        if str in possible_rates:
            return str

diler_rate_str = None
while True:
    name = input("Print new player name:").strip()
    if name == "No new players":
        break
    if name == "Diler":
        if diler_rate_str is not None:
            print("Diler is already in the game")
            continue
        diler_rate_str = random.choice(possible_rates)
        print("Diler rate is " + diler_rate_str)
        continue
    add_player(name, get_rate())

if diler_rate_str is not None:
    add_player("Diler", diler_rate_str)
results = get_random_game_result([p.rate for p in players])
print(f"\n\n\nThe number on the roulette wheel is {results.result_number}")

for i, res in enumerate(results.is_winner):
    print(players[i].name, end='')
    if results.is_winner[i]:
        print(" won the bet")
    else:
        print(" lost the bet")