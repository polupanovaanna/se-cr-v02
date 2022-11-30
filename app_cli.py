from main import *


possible_rates = ["VoisinsDeZero", "Tier", "Orphelins", "Parity 1", "Parity 0", "Color R", "Color G", "Color B"]

rate_list = []
names = []
dilet_rate = None

def get_rate():
    str = input("Print new player rate:").strip()
    if str in possible_rates:
        return str
    while True:
        str = input("Print RIGHT new player rate:").strip()
        if str in possible_rates:
            return str

while True:
    name = input("Print new player name:").strip()
    if name == "No new players":
        break
    if name == "Diler":
        if dilet_rate is not None:
            print("Diler is already in the game")
            continue
        diler_rate_str = random.choice(possible_rates)
        print("Diler rate is " + diler_rate_str)
        dilet_rate = convert_string_to_rate(diler_rate_str)
        continue
    s = get_rate()
    rate_list.append(convert_string_to_rate(s))
    names.append(name)

if dilet_rate is not None:
    rate_list.append(dilet_rate)
    names.append("Diler")
results = get_random_game_result(rate_list)
print(f"\n\n\nThe number on the roulette wheel is {results.result_number}")

for i, res in enumerate(results.is_winner):
    print(names[i], end='')
    if results.is_winner[i]:
        print(" won the bet")
    else:
        print(" lost the bet")